class Square:
    def __init__(self, s=1):
        self.side = s

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return float(round(self.side * 4, 2))

    def __str__(self):
        return f'Это квадрат со стороной {self.side}'

    def __eq__(self, other):
        return self.side == other.side

    # def __ge__(self, other):
    #     return self.side > other.side

sq1= Square(5)
sq2= Square(5)
# print(sq1)
# print(sq2)
sravn= (sq1 == sq2)
print(f'Эти квадраты: {sravn}')