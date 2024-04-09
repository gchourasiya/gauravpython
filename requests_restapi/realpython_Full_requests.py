import requests
from requests.exceptions import HTTPError
'''
resp = requests.get('https://api.github.com')
print(resp.text)
'''
'''
for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        # print(response.headers)

        response.raise_for_status()

    except HTTPError as http_err:
        print(f'HTTP status error happened:{http_err}')

    except Exception as e:
        print(f'Other exception : {e}')
    else:
        print("Success")

'''
url = 'https://api.github.com/search/repositories'
response = requests.get(url,params={'q':'requests+language:python'})
json_response = response.json()