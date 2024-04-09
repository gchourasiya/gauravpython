import urllib.parse
params = {'q': 'Python URL encoding', 'as_sitesearch': 'www.urlencoder.io'}
out = urllib.parse.urlencode(params,quote_via=urllib.parse.quote_plus)
# out = urllib.parse.urlencode(params)
print(out)




params = {'name': 'Rajeev Singh', 'phone': ['+919999999999', '+628888888888']}

out = urllib.parse.urlencode(params)#, doseq=True)
print(out)

out = urllib.parse.urlencode(params, doseq=True)
print(out)