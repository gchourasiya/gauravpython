# Python program to
# demonstrate protected members

# Creating a base class
class Base:
    def __init__(self):
        # Protected member
        self._a = 2
        # print(self._a)


class Derived(Base):
    def __init__(self):


        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ",self._a)
        # Modify the protected variable:
        self._a = 3
        print("Calling modified protected member outside class: ",
              self._a)
derObj = Derived()
baseObj = Base()
print('\n')
# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", derObj._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", baseObj._a)
