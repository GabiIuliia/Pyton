# while True:
#     a= input('Введите первое число: ')
#     b= input('Введите второе число: ')
#     if a.isdigit() and b.isdigit():
#         if int(b) == 0:
#             print()
#         else:
#             print(int(a)/int(b))
#             break
#     else:
#         print('Необходимо вводить тольок целые числа')
from wsgiref.validate import assert_

while True:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    try:
        a = int(a)
        b = int(b)
        result = a / b
    except ValueError:
        print('Вас просят ввести целове число')
    except ZeroDivisionError:
        print('Вас просят ввести целове число')
    else:
        print('Вас просят ввести целове число')
        break

