# Цикл While
import turtle as t

"""
sides = 6  # число сторон фигуры
dist = 100  # длина стороны фигуры
angle = 360 / sides  # угол поворота
count = 0  # счетчик числа "витков" цикла

while count < sides:
    t.forward(dist)
    t.right(angle)
    count +=1
    # count = count + 1 равно count +=1 инкремент счетчика
    # count = count - 1 равно count -=1 декремент счетчика (уменьшение на 1)
    # count = count / 1 равно count /=1
    # count = count * 1 равно count *=1
else:
    print ('Цикл завершен') # else писать не обязательно
t.mainloop()"""


sides = 6  # число сторон фигуры
dist = 50  # длина стороны фигуры
angle = 360 / sides  # угол поворота
count = 0  # счетчик числа "витков" цикла
sq_count= 5 #счетчик числа сторон квадрата

t.speed(1)
while count < sides:
    sq_count=0 #обнуляем счетчик сторон квадрата
    while sq_count <4: #внутренний цикл
        t.forward(dist) #вложенный цикл
        t.right(90)
        sq_count+=1
    t.right (angle)
    count +=1 #инкремент счетчика вн. цикла (увеличение на 1)
    # count = count + 1 равно count +=1 инкремент счетчика
    # count = count - 1 равно count -=1 декремент счетчика (уменьшение на 1)
    # count = count / 1 равно count /=1
    # count = count * 1 равно count *=1

t.mainloop()
