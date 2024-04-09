import requests

s = requests.Session()
s.auth = ('login', 'password')
s.headers.update({'Accept': 'application/json'})

# r = s.get('https://reqbin.com/echo/get/json')
r = s.post('https://reqbin.com/echo/post/json')

print(f'Status Code: {r.status_code}, Content: {r.json()}')