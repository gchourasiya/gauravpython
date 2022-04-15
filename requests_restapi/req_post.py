import requests
url = "https://reqres.in/api/users'"

data = {'key':'value'}
response = requests.post(url=url,data=data)
print(response.json())

print(response.headers["date"])
print(response)

