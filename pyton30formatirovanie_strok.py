# Форматирование строк интерпаляция строк
from tkinter.font import names

name = 'Виктор'
age = 9
height = 141.5678
# метод плейсхолдеров
# f_string='%18s,\nвозраст: %2d,\nрост:%6.1f см' %(name,age,height)
# print(f_string)


# метод строки формат (format) именованные аргументы)
f_string = 'Имя:{N}, возраст:{V}, рост: {R}'.format(N=name, V=age, R=height)
print(f_string)


#метод строки формат (format) позиционные аргументы)
f_string = 'Имя:{0}, возраст:{1}, рост: {2}'.format(name, age, height)
print(f_string)

#метод строки формат (format) позиционные аргументы и плейс холдеры
f_string = 'Имя:{:s}, возраст:{:d}, рост: {:.2f}'.format(name, age, height)
print(f_string)

#интерполяция строк (f-строка)
f_string=f'Имя:{name}, Возраст:{age}, Рост: {height:.3f}'
f_string += f'При фигуре из 4 сторон угол будеет:{360/4}'
print(f_string)