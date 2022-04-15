def smart_divide(func):
    def inner(a,b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return      #Returns None and exits the current function.

        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    return a/b


out = divide(5,1)
print(out)