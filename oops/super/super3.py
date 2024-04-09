class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length,length)

sqr = Square(4)
print(sqr.area())
print(sqr.perimeter())
print('****************************')
rec = Rectangle(2,4)
print(rec.area())
print(rec.perimeter())

