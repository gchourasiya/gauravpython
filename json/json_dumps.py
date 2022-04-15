import json

person_dict = {'name': 'Bob',
'age': 12,
'children': None
}


person_json= json.dumps(person_dict)
print(person_json)      #{"name": "Bob", "age": 12, "children": null}

print(type(person_json))    #<class 'str'>

