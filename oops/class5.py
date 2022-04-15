class A():
    def temp(self):
        print('in Class A')

class B():
    def temp(self):
        print('in class B')

class C(A, B):
    pass

obj = C()
obj.temp()
obj.temp()