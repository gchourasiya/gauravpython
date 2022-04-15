#Sorting a dict based on one of the multiple values of key
t={'Name1':{"Jf":0.89,"Date":"09-10-2018"},'Name2':{"Jf":0.77,"Date":"09-11-2018"}}
sorted_dict = sorted(t.items(),key=lambda x:x[1]['Date'])
# print(sorted_dict)

#How do I sort a list of dictionaries by a value of the dictionary?
original_list = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
expected_list = [{'name':'Bart', 'age':10}, {'name':'Homer', 'age':39}]
output = sorted(original_list,key=lambda x:x['name'])
# print(output)



# using sorted and lambda to print list sorted by age
lis = [{"name": "Nandini", "age": 21},
       {"name": "Panjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

output = sorted(lis,key=lambda x:(x['name'],x['age']),reverse=True)
# print(output)



#explaination sorting
english_spanish = {"hi": "hola", "thanks": "gracias", "yes": "si", "no": "no"}
dict = sorted(english_spanish.items(),key=lambda x:x[1])
print(dict)
for key, value in sorted(english_spanish.items(), key = lambda value: value[1]):
        print(key, value)


#Convert lists to dict
keys = ['name', 'age', 'food']
values = ['Monty', 42, 'spam']
expected_dict = {'name': 'Monty', 'age': 42, 'food': 'spam'}
'''
#Long approach
expected_dict1 = {}
for i in range(len(keys)):
    for j in range(len(values)):
        if i ==j:
            expected_dict1[keys[i]]=values[j]
print(expected_dict1)
'''
#Quick Approach ==> refer to dict_zip.py
#Quick Approach ==> refer to dict_zip.py


