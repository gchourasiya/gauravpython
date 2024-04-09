import requests

s = requests.Session()
s.auth = ('user','pass')

s.headers.update({'x-test':'true'})
s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})
print(s.headers)


