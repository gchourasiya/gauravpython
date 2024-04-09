# Python program to
# demonstrate private members

# Creating a Base class


class Base(object):
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"

class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")

        print(self.a)
        print(self.__c)

derobj = Derived()
# print(derobj.a)