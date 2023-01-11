class Rectangle:
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height
    
    @property
    def area(self):
        return self._width * self.height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def __str__(self) -> str:
        return f"Width: {self.width}, Height: {self.height}"

def use_it(rc: Rectangle):
    """This only works on a Rectangle, and not on any derived class"""
    w = rc.width
    rc.height = 10 # Problem
    expected = int(w * 10)
    print(f"Expected an area of {expected}, but got {rc.area}")

rc = Rectangle(2, 3)
use_it(rc)

# Side effect of breaking the Liskov Principle
class Square(Rectangle):
    def __init__(self, size) -> None:
        super().__init__(width=size, height=size)

    @Rectangle.width.setter # Violates LP
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter # Violates LP
    def height(self, value):
        self._height = self._width = value

square = Square(5)
# Won't work fopr derived Square class -> breaks LP
use_it(square)

# To fix this broken principle, it is up to you...
# You may decide that there's no reason to have the Square class and instead
# add some sort of boolean property on the Rectangle that tells you it's a square...

# Or perhaps you could have a Factory Method -  there are many ways to address this
# broken principle example.