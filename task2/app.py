from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from bson import ObjectId
from envparse import Env

app = Flask(__name__)
env = Env()

# Get the MongoDB URI from environment variables
app.config["MONGO_URI"] = env.str("MONGODB_URL", default="mongodb://localhost:27017/test_database")
# Create a PyMongo instance
mongo = PyMongo(app)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/api/resource/", methods=["GET", "POST", "PUT", "DELETE"])
def resource():
    # Handle GET request
    if request.method == "GET":
        collection = mongo.db.data
        resources = list(collection.find({}))
        return jsonify(str(resources))

    # Handle POST request
    elif request.method == "POST":
        collection = mongo.db.data
        data = request.get_json()
        result = collection.insert_one(data)
        return jsonify({"message": "Resource created", "id": str(result.inserted_id)})

    # Handle PUT request
    elif request.method == "PUT":
        collection = mongo.db.data
        data = request.get_json()

        # Extract resource_id from request arguments
        resource_id = request.args.get("resource_id")

        if not ObjectId.is_valid(resource_id):  # validation of id
            return jsonify({"message": "Invalid resource ID"}), 400

        result = collection.update_one({"_id": ObjectId(resource_id)}, {"$set": data})

        if result.modified_count != 0:  # check what's db been updated
            return jsonify({"message": "Resource updated"})

        return jsonify({"message": "Resource not found"}), 404

    # Handle DELETE request
    elif request.method == "DELETE":
        collection = mongo.db.data
        resource_id = request.args.get("resource_id")

        if not ObjectId.is_valid(resource_id):
            return jsonify({"message": "Invalid resource ID"}), 400

        result = collection.delete_one({"_id": ObjectId(resource_id)})

        if result.deleted_count == 0:
            return jsonify({"message": "Resource not found"}), 404

        return jsonify({"message": "Resource deleted"})

    # Handle any other request method
    else:
        return jsonify({"result": "Error, something went wrong!"})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
