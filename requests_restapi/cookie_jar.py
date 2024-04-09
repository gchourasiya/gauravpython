import requests

session = requests.session()
my_cookies = {'cookie_key': 'cookie_value',
              'another_cookie_key': 'another_cookie_value'}
requests.utils.add_dict_to_cookiejar(session.cookies, my_cookies)