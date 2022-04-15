import copy

a = [1, 2, 3]
b = [4, 5, 6]
c = ['a', 'b']

# print("Using normal assignment operatings to copy:")
#
# d = c
# d.append('d')
# print (id(c) == id(d))          # True - d is the same object as c
# print (id(c[0]) == id(d[0]))    # True - d[0] is the same object as c[0]
# print(c)
# print(d)
#
print("\n\nUsing a shallow copy:")

d = copy.copy(c)
print (id(c) == id(d))          # False - d is now a new object
print (id(c[0]) == id(d[0]))    # True - d[0] is the same object as c[0]
print(c)
print(d)
#
# print("\n\nUsing a deep copy:")
#
# d = copy.deepcopy(c)
# print(id(c) == id(d))          # False - d is now a new object
# print(id(c[0]) == id(d[0]))    # False - d[0] is now a new object
# print(c)
# print(d)

print("\n\nUsing a : copy")

d = c[:]
print(id(c) == id(d))          # False - d is now a new object
print(id(c[0]) == id(d[0]))    # False - d[0] is now a new object
print(c)
print(d)

#Copy with the colon slice, is actually a shallow copy,
# it copies only the reference of the nested list.
# To make sure that all nested structures are copied
# and become independent of the original, you must use copy.deepcopy() function.