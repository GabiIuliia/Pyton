# Объектно-ориентированное програмирование (объектно-ориентированный подход)
# Инкапсуляция


class Ball:
    def __init__(self, d=1, color='желтый'):
        #  Спец. методы. Поле класса, имеет self и принадлежит класcу, члены класса
        self.diametr = d
        self.color = color
        print('Это мяч')

    # Метод класса
    def info(self):
        print('Мяч имеет цвет:', self.color)
        print('Размер мяча:', self.diametr)


ball1 = Ball(5, 'красный')  # ball1- экземпляр класса Ball #1
ball2 = Ball(10, 'синий')  # ball1- экземпляр класса Ball #1
ball3 = Ball()


print(id(ball1))
print(id(ball2))


ball1.info()
ball2.info()
ball3.info()


# print(ball1.diametr, ball1.color)
# print(ball2.diametr, ball2.color)
