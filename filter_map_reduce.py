from functools import reduce
items = [1, 2, 3, 4, 5]

output = list(filter(lambda x:x%2 == 0,items))
print(output)

output = list(map(lambda x:x*x,items))
print(output)

output = reduce(lambda x,y:x*y,items)
print(output)

add = lambda x, y: x + y
print(add(2, 3))


x = list(map(lambda a: a**2, [1, 2, 3, 4, 5]))
print(x)

y = list(map(lambda a, b: a+b, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
print(y)


lst = [{'name': 'Bob', 'age': 30}, {'name': 'Matt', 'age': 40}]
zip = list(map(lambda x:x['name'],lst))
print(zip)

