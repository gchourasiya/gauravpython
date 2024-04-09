'''
Method Resolution Order (MRO)
Method Resolution Order (MRO) is the order in which methods
should be inherited in the presence of multiple inheritance. You can view the MRO by using the __mro__ attribute.
'''

class Animal:
  def __init__(self, Animal):
    print(Animal, 'is an animal.')


class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)

class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammal):
    print(NonWingedMammal, "can't fly.")
    super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammal):
    print(NonMarineMammal, "can't swim.")
    super().__init__(NonMarineMammal)


class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.')
    super().__init__('Dog')

# d = Dog()
# print('')
print(Dog.__mro__)

