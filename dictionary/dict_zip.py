#Convert lists to dict
keys = ['name', 'age', 'food']
values = ['Monty', 42, 'spam']
expected_dict = {'name': 'Monty', 'age': 42, 'food': 'spam'}

new_dict = dict(zip(keys,values))
print(new_dict)