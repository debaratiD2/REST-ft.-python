#post()
# requires a URL and includes headers and data as arguments
#The principle is that your data will be sent to the API endpoint, and the server will process it and return a response. This is commonly used for creating new resources or submitting data to the server.

#example-1
import requests
response = requests.post(
    "https://api.example.com/endpoint",
    headers={
        "Content-Type": "application/json"
    },
    json={
        "key1": "value1",
        "key2": "value2"
    }
)

#example-2

import requests

response = requests.post(
    
    "https://jsonplaceholder.typicode.com/users",
    headers = {
        "Content-Type": "application/json"
    },
    json = {
        "name": "James Shelby",
        "email": "jamesshelbys1987@example.com",
        "username":"jshelby1987"
    }

)

print("Status Code:", response.status_code)
print("Response:", response.json())