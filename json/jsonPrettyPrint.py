import json

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'        #Data type string

person_dict = json.loads(person_string)
print(type((person_dict)))

print(json.dumps(person_dict,indent=4,sort_keys=True))



