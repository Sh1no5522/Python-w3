class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length
class Rectangle(Square):
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def areaw(self):
        return self.length * self.width
            


shape = Shape()
print(shape.area())

square = Square(12)
print(square.area())

square2 = Rectangle(12,10)
print(square2.areaw())