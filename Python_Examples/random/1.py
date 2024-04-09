'''
Python Program to Generate Random Numbers
'''

import random
lst = []
while len(lst)<101:
    num = random.randint(0, 100)
    if num in lst:
        continue
    else:
        lst.append(num)
    lst.sort()

print(lst)