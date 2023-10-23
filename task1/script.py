import psutil
import requests

memory_threshold = 90

api_url = "https://api.com/alert"


def check_memory_usage():
    memory_percent = psutil.virtual_memory().percent
    if memory_percent > memory_threshold:
        send_alert()


def send_alert():
    data = {"message": "Memory usage exceeded the threshold"}
    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        print("Alert sent successfully")
    else:
        print(f"Failed to send alert. Status code: {response.status_code}")


if __name__ == "__main__":
    check_memory_usage()
