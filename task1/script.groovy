@Grab(group='org.codehaus.groovy.modules.http-builder', module='http-builder', version='0.7.1')

import groovyx.net.http.RESTClient

def memoryThreshold = 90

def apiUrl = "https://your-api.com/alert"

def checkMemoryUsage() {
    def memoryInfo = "free -m".execute().text
    def memoryUsage = memoryInfo.split()[8].toInteger() / memoryInfo.split()[7].toInteger() * 100

    if (memoryUsage > memoryThreshold) {
        sendAlert()
    }
}

def sendAlert() {
    def client = new RESTClient(apiUrl)
    def requestBody = [message: "Memory usage exceeded the threshold"]
    def response = client.post(contentType: "application/json") {
        json requestBody
    }

    if (response.status == 200) {
        println("Alert sent successfully")
    } else {
        println("Failed to send alert. Status code: ${response.status}")
    }
}

checkMemoryUsage()
