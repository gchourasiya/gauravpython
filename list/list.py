import copy
a = [1,2,3,4,5,5]

a.append(7)
print(a)

# a.clear()
print(a)

# b = a.copy()
b = copy.copy(a)
a.append(10)
print(id(a))
print(id(b))
print(a)
print(b)

#sort and sorted
a = [4,1,23,4,7,8,9]
a.sort()        #Inplace sorting
print(a)
b = sorted(a)
print(b)


