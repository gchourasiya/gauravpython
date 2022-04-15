import requests
url = "https://reqres.in/api/users'"

data = {'key':'value'}
response = requests.put(url=url,data=data)
print(response.json())