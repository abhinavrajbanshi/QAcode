#Create Post
import requests
url="https://jsonplaceholder.typicode.com/posts"
payload= {
    "userId": 1,
    "title": "API Automation",
    "body": "This is api automation"
  }
response=requests.post(url, json=payload)
print(response.json())
print(response.status_code)

status_code=response.status_code
if status_code==201:
    print("Request is successfull")
else:
    print("Request is unsucessfull")
assert status_code==201
print("Request Daami")
