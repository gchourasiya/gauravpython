original = [1, 2, 3]
other = original
original[:] = [0, 0] # changes the contents of the list that both
                         # original and other refer to
# original = [0,0]
print(other) # see below, now you can see the change through other
'''
This syntax is a slice assignment. A slice of [:] means the entire list.
The difference between nums[:] = and nums = is that the latter doesn't replace elements in 
the original list. This is observable when there are two references to the list 
'''