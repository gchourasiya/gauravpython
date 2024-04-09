'''
A callable object is one which can be called like a function.
In Python, __call__() is used to resolve the code associated with a callable object.
Any object can be converted to a callable object just by writing it in a function call format.
An object of that kind invokes the __call__() method and executes the code associated with it.

'''

class A:
    def __init__(self, x):
        print("inside __init__()")
        self.y = x

    def __str__(self):
        print("inside __str__()")
        print("value of y:", str(self.y))

    def __call__(self):
        res = 0
        print("inside __call__()")
        print("adding 2 to the value of y")
        res = self.y + 2
        return res

a = A(3)
a.__str__()
out = a()
print(out)
