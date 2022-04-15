def fib(limit):
    a,b=0,1
    while a < limit:
        yield a
        a,b = b,a+b


#Approach1
for i in fib(10):
    print(i)
#Generator objects are used either by calling the
# next method on the generator object or using the generator object in a “for in” loop

print("\ntrying approach 2")
#Approach 2
x= fib(5)
while True:
    try:
        print(next(x))
    except StopIteration:
        break
