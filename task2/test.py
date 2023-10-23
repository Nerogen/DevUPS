import requests  # Import the requests library to make HTTP requests

# Define data to be used in the POST request
data = {
    "key1": "value1",
    "key2": "value2"
}

# Send a POST request to create a new resource
response = requests.post("http://localhost:5000/api/resource/", json=data)
print(response.json())  # Print the JSON response from the server

# Extract the 'id' from the POST response for later use
resource_id = response.json().get("id")

# Send a GET request to retrieve a list of resources
response = requests.get("http://localhost:5000/api/resource/")
print(response.json())  # Print the JSON response from the server

# Define data to be used in the PUT request to update the resource
data = {
    "key1": "new_value1",
    "key2": "new_value2"
}

# Send a PUT request to update an existing resource using the resource_id
response = requests.put(f"http://localhost:5000/api/resource/?resource_id={resource_id}", json=data)
print(response.json())  # Print the JSON response from the server

# Send a DELETE request to delete the resource with the specified resource_id
response = requests.delete(f"http://localhost:5000/api/resource/?resource_id={resource_id}")
print(response.json())  # Print the JSON response from the server
