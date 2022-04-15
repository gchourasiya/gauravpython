def inc(x):
    return x + 1


def dec(x):
    return x - 1

def operate(func,x):
    output=func(x)
    return output

print(operate(inc,3))
print(operate(dec,3))
