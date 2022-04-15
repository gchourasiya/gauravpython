class Dog:
    animal ='Dog'
    def __init__(self,breed,color):
        self.breed = breed
        self.color = color


Rodger= Dog("Wishdoggy","Brown")
print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print(Dog.animal)

