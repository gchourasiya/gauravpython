'''
#1. Check if a list contains an element
li = [1,2,3,'a','b','c']
print('a' in li)


#2.How to iterate over 2+ lists at the same time

name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]
z = zip(name,animal,age)
for i in z:
    print(i)
    print(type(i))

#4. Is a list mutable?
x = [1]

x.append(5)
x.extend([6,7])
print(id(x),':',x)
'''
