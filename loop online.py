# Цикличное выполнение программы
from random import choice

choice = ''  # инициализация выбора пользователя

while choice != 'Q':
    choice = input('Введите R чтобы повернуть направо или L чтобы повернуть налево')
    if choice == 'L' or choice == 'l':
        print('Вы повернули налево', choice)
    if choice == 'R' or choice == 'r':
            print('Вы повернули направо', choice)
    else:
    print('Вы продолжили движение прямо', choice)
else: print('Всего доброго')
