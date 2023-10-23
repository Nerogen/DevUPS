#!/bin/bash


memory_threshold=90

api_url="https://your-api.com/alert"

check_memory_usage() {
    memory_percent=$(free | grep Mem | awk '{print $3/$2 * 100}')
    if (( $(bc <<< "$memory_percent > $memory_threshold") )); then
        send_alert
    fi
}

send_alert() {
    message="Memory usage exceeded the threshold"
    curl -X POST -H "Content-Type: application/json" -d "{\"message\": \"$message\"}" $api_url
    if [ $? -eq 0 ]; then
        echo "Alert sent successfully"
    else
        echo "Failed to send alert"
    fi
}

check_memory_usage
