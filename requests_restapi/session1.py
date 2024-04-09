import requests
url1 ="https://httpbin.org/cookies/set/sessioncookie/123456789"
url2 = "https://httpbin.org/cookies"

s = requests.Session()
s.get(url1)
# print(output)
# print(output.status_code)
# print(output.json())
# print(output.content)

output2= s.get(url2)
print(output2.text)