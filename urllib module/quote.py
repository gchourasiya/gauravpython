import urllib.parse

query = 'Hello World@+Python'
out = urllib.parse.quote(query)
print(out)



# the quote() function considers / character safe by default.
# That means, It doesn’t encode / character -
print(urllib.parse.quote('/'))

#The quote() function accepts a named parameter called safe whose default value is /.
# If you want to encode / character as well, then you can do so by supplying an
# empty string in the safe parameter like this-
print(urllib.parse.quote('/', safe=''))
