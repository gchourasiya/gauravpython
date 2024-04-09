'''
Without patch and mock
Refer to 5.py for mock and patch.
'''

import requests
url = "http://www.google.com"

def is_valid_url(url):
    try:
        resp = requests.get(url)
    except Exception:
        return False
    return resp.status_code ==200


def test_is_valid_url():
    assert is_valid_url(url) is True
    assert is_valid_url('http://agiliq.com/eerwweeee') is False # We want False in 404 pages too
    assert is_valid_url('http://aeewererr.com') is False

test_is_valid_url()
