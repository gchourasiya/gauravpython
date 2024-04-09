#Convert lists to dict
keys = ['name', 'age', 'food']
values = ['Monty', 42, 'spam']
expected_dict = {'name': 'Monty', 'age': 42, 'food': 'spam'}

new_dict = dict(zip(keys,values))
print(new_dict)

print(dict([[1,2],[3,4]]))
#Dict of Lists

print(dict([(3,26),(4,44)]))
#Dict of tuples