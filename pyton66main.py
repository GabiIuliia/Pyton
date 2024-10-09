# Импортирование файлов
from pyton66 import Square

if __name__ == '__main__':
    sq1 = Square(10)
    sq2 = Square(6)
    complex_sq = [Square(2), Square(3)]

    square = sq1 - sq2
    print(square)
    square = sq1 + sq2
    print(square)
    print(complex_sq)
    print(sq1 == sq2)
    print(sq1 >= sq2)
