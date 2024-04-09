class Employee:
    ecount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.ecount += 1

    def __del__(self):
        Employee.ecount -= 1

    @staticmethod
    def displayCount():
        print("Count = ", Employee.ecount)

emp1 = Employee("Rahul",3000)
emp1.displayCount()
Employee.displayCount()

print(hasattr(emp1,'age'))
setattr(emp1,'age',30)
print(getattr(emp1,'age'))
delattr(emp1,'salary')
print(getattr(emp1,'salary'))




