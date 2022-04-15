class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False

class Employee(Person):
    def isEmployee(self):
        return True


emp1 = Person("Geek1")  # An Object of Person
print(emp1.getName(),emp1.isEmployee())

emp2 = Employee("Geek2") # An Object of Employee
print(emp2.getName(),emp2.isEmployee())