def simpleGen():
    yield 1
    yield 2
    yield 3

x=simpleGen()
while True:
    try:
        print(next(x))
    except StopIteration:
        break