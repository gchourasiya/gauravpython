import requests
url = "https://reqres.in/api/users"

params = {'page':1}

# resp = requests.get(url, params=params)
# print(resp.json())
# print(resp.headers)

should_fetch_next_page = True
while should_fetch_next_page:
    print(f"Trying to see if page {params['page']} can be fetched...")
    resp = requests.get(url, params=params)
    if resp.json()['data']:
        params['page']+=1
        print(resp.json())
    else:
        should_fetch_next_page = False
        print("Page#" ,params['page']-1," is the last page.")



