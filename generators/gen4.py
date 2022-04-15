def simplegen():
    yield 1
    yield 2
    yield 3

x = simplegen()
for i in x:
    print(i)