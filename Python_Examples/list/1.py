'''
Count Even/Odd Numbers in a List of 10 Elements
Count Even/Odd Numbers in a List of n Elements
'''

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evncount = 0
oddcount =0
for i in lst:
    if i%2==0:
        evncount+=1
    else:
        oddcount+=1

print(evncount,oddcount)