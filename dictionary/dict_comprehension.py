#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
dollar_to_pound = 0.76
new_price = {key:0.76*value for key,value in old_price.items()}
print(new_price)            #{'milk': 0.7752, 'coffee': 1.9, 'bread': 1.9}


#Example 4: If Conditional Dictionary Comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
even_dict = {key:value for key,value in original_dict.items() if value%2==0}
print(even_dict)            #{'jack': 38, 'michael': 48}


#Example 5: Multiple if Conditional Dictionary Comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict = {key:value for key,value in original_dict.items() if value%2==0 and value<40}
print(new_dict)             #{'jack': 38}


#Example 6: if-else Conditional Dictionary Comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict1 = {key:('old' if value>40 else 'young') for key,value in original_dict.items()}
print(new_dict1)

#Nested Dictionary Comprehension
dictionary = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
}
print(dictionary)


