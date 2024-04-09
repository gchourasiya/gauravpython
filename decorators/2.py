def inc(x):
    return x + 1


def dec(x):
    return x - 1

def operate(func,x):
    output=func(x)
    return output

# print(operate(inc,3))
# print(operate(dec,3))

out1 = operate(inc,3)
print(out1)