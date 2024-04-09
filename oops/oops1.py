class Employee:
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	def displayEmployee(self):
		print ("Name : ", self.name)
		print ("Salary: ", self.salary)

emp = Employee('Rahul',30)
emp.displayEmployee()

