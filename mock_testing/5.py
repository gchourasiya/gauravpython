import requests
from unittest.mock import patch,Mock
url = "http://www.google.com"

def is_valid_url(url):
    try:
        resp = requests.get(url)
    except Exception:
        return False
    return resp.status_code ==200

@patch('5.requests')
def test_is_valid_url(patched_requests):
    patched_requests.get.return_value = Mock(status_code=200)
    assert is_valid_url(url) is True
    patched_requests.get = Mock(side_effect=Exception)
    assert is_valid_url("http://www.gogle.cme") is False

test_is_valid_url()
