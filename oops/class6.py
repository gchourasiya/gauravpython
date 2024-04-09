class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print(blu.species)
print(blu.name)


class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')

print(Person.age)
print(Person.greet)
