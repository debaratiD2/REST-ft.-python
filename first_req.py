import requests
# Write code here
response = requests.get("https://reqres.in")
# Don't change below this line
print(response.status_code)
print(response.url)