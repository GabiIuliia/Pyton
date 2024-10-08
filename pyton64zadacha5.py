# Полиморфизм

from math import pi


class Square:
    def __init__(self, s):
        self.side = s

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return float(round(self.side * 4, 2))


class Circle:
    def __init__(self):
        self.perimeter()

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return round(2 * pi * self.radius)


class Rectangle:
    def __init__(self, w, h):
        self.wight = w
        self.hight = h

    def area(self):
        return self.wight * self.hight

    def perimeter(self):
        return round((self.wight + self.hight) * 2, 1)


circle = Circle(5)
square = Square(10)
rect = Rectangle(5, 7)

print(circle.perimeter())
print(square.perimeter())
print(rect.perimeter())

if rect.__class__.__name__ == 'Rectangle':
    print('Это экземпляр Rectangle')
