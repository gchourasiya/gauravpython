#Create a new JSON file from an existing JSON file
import json
with open('person.json','r') as file:
    d = json.load(file)

data = {key: [ele for ele in val if not 'French' in ele] for key, val in d.items()}
print(data)