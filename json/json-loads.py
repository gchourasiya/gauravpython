import json
p = '{"name": "Bob", "languages": ["Python", "Java"]}'

outcome = json.loads(p)
print(outcome)          #{'name': 'Bob', 'languages': ['Python', 'Java']}
print(type(outcome))    #<class 'dict'>
print(outcome['languages'])     #['Python', 'Java']

