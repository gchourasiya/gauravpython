import requests
# url = "http://api.open-notify.org/astros.json"
# response = requests.get(url)
# data =response.json()
# text = response.text
# print(text)
#
# reason = response.reason
# print(reason)
#
# status = response.status_code
# print(status)
#
# content = response.content
# print(content)
#

# for data in data['people']:
#     if data['craft']== 'ISS':
#         print(data['name'])
'''
query = {'lat':'45', 'lon':'180'}
response = requests.get(url="http://api.open-notify.org/iss-pass.json",params=query)
print(response.json())
'''


my_headers = {'Authorization' : 'Bearer {access_token}'}
response = requests.get('http://httpbin.org/headers', headers=my_headers)
print(response.json())

