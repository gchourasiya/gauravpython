import json

jsonfile = r'person.json'

with open(jsonfile,'r') as jsonfile:        #File Handling

    data = json.load(jsonfile)              #Json Handling
    print(data)
    print(type(data))