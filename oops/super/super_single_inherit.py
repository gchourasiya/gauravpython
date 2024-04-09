class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')

class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Dog')
    #OR instead of super below can also be called
    #Mammal.__init__(self,'Dog')

dog = Dog()