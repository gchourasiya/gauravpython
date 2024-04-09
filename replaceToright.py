#Replace element to the right with the greatest element

Lst = [16,17,4,3,5,2]

max = Lst[-1]
Lst[-1] =-1
for i in range(len(Lst)-2,-1,-1):
    temp = Lst[i]
    Lst[i]=max
    if max < temp:
        max = temp
for i in range(len(Lst)):
    print(Lst[i],end = ' ')
