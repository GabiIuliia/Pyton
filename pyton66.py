# Импортирование файлов
# Классы фигур (наследование)
# Родительский (базовый) класс (superclass)
# Дочерний (производный, наследник) класс

from math import pi


class Rectangle:
    def __init__(self, w, h):
        self.wight = w
        self.hight = h

    def area(self):
        return self.wight * self.hight

    def perimeter(self):
        return round((self.wight + self.hight) * 2, 1)

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return float(round(self.side * 4, 2))

    # Геттер отвечает за получение чего-то , "верни мне ширину чтобы ее получить"
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    # Сеттер установать что-то, "установи новое значение"
    def set_width(self, new_w):
        self.width = new_w

    def set_height(self, new_h):
        self.height = new_h

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


class Square(Rectangle):
    def __init__(self, s=1):
        super().__init__(s, s)
        self.side = s


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return round(2 * pi * self.radius, 1)
