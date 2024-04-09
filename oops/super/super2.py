class Computer():
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd

class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
        super().__init__(computer,ram,ssd)
        self.model = model
        print("We are in sub-class.")

pc = Laptop('Lenovo',16,512,'Chinese')
