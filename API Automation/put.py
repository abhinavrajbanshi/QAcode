import requests
url="https://jsonplaceholder.typicode.com/posts/1"
payload= {
    "userId": 1,
    "title": "API Automation",
    "body": "This is api automation"
  }
response=requests.put(url, json=payload)
print(response.json())
print(response.status_code)

status_code=response.status_code
if status_code==200:
    print("Request is updated")
else:
    print("Request is not updated")
assert status_code==200
print("Request Daami")
