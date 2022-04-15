import json

json_file = r'products.json'

with open(json_file,'r') as jsonfile:        #File Handling
    data = json.load(jsonfile)              #Json Handling
    for i in data:
        print(i)