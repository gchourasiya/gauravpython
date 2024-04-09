from bs4 import BeautifulSoup
import requests

# Make the request
url = 'https://crawler-test.com/'
r = requests.get(url)

# print(r.text[:500])

# Parse the HTML
soup = BeautifulSoup(r.text, 'html.parser')
print(soup)