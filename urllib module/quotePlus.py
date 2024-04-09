import urllib.parse
query = 'Hello World@+Python'

out = urllib.parse.quote_plus(query)
print(out)