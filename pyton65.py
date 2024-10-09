#Объектно-ориентированный подход


class Square:
    def __init__(self, s=1):
        self.side = s

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return float(round(self.side * 4, 2))

    def __str__(self):  # Представление простого объекта в виде строки
        return f'Это квадрат со стороной {self.side}'

    def __eq__(self, other):
        return self.side == other.side

    def __ge__(self, other):
        return self.side >= other.side

    def __add__(self, other):
        return self.side + other.side

    def __sub__(self, other):
        return self.side - other.side

    def __repr__(self):  # Представление сложного объекта в виде строки
        return f'Квадрат со стороной {self.side}'


    def __del__(self):
        print(f'Квадрат со стороной {self.side} стерт!')


sq1 = Square(4)
sq2 = Square(5)
complex_sq= [Square(2),Square(3)]
square = sq1 - sq2
print(square)
square = sq1 + sq2
print(square)

# print(sq1)
# print(sq2)
sravn = (sq1 == sq2)
print(f'Эти квадраты: {sravn}')
