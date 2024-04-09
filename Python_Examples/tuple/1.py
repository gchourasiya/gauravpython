'''
Python Program to Reverse a Tuple
'''

tup =(11, 22, 33, 44, 55)
lst=[]
tuplen =len(tup)
for i in range(-1,-1*(tuplen+1),-1):
    lst.append(tup[i])

final_tup = tuple(lst)
print(final_tup)



tup =(11, 22, 33, 44, 55)
tupl2 = tuple(tup[::-1])
print(type(tupl2))
