# "Бросаемся" исключениями (throw (Java,C++, C#)->raise)


min_val=1
max_val=10




try:
    cur_val= int(input(f'Введите целое число от {min_val}  до {max_val}: '))
    if cur_val == 0:
        raise  ValueError ('не вводи ноль')
    if not min_val<=cur_val<=max_val:
        raise ValueError('Введеное число вне диапазона')

    print(f'Вы ввели {cur_val} целое число которое в диапазоне от {min_val}  до {max_val}: ')

except ValueError as exp: #ошибка  вначении
        print('Нужно быть повнимательнее', exp)
        print('Попробуйте снова')