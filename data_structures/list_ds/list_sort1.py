# How to sort them based on their length
names=['hari','aruna','jai','di']
names.sort(key=len)
print(names)


#how to sort the data in descending order

names.sort(key=len,reverse=True)
print(names)


sortedNames = sorted(names)
print(sortedNames)
