# x = [i for i in range(1,100) if i!=1 and not any(i%j==0 for j in range(2,i))]
#OR
x = [num for num in range(1,100) if num!=1 and not any ([div for div in range(2,num) if num%div==0])]

x.insert(0,1)
print(x)