#

choice = ''  # инициализация выбора пользователя
work = True
while work:
    choice = input('Введите R чтобы повернуть направо или L чтобы повернуть налево:')
    if choice == 'L' or choice == 'l':
        print('Вы повернули налево', choice)
    if choice == 'R' or choice == 'r':
        print('Вы повернули направо', choice)
    if choice == 'Q':
        work = not work  # инвертировали значение
    else:
        print('Вы продолжили движение прямо', choice)
else:
    print('Всего доброго')
