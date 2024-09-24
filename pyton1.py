print(3 + 5)

print(2, 5, 63.3, 'кафе "Аист"')
#2 это целое число (int)
#62.5 это вещественное число (float)
#'строка' это это строка (str)

import turtle as t  # подключили черепашку
#RAM- random access memory
#DRY-do not repead  yourself (code should be clear)
dist = 100 # переменной dist присвоено значение 100
sides = 10 #число сторон замкнутой фигуры
angel = 360 / sides # переменной angel присвоено: угол как 360/sides



t.forward(dist)
t.right(angel)
t.forward(dist)

t.mainloop()

