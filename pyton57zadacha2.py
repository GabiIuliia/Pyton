# вечный цикл, который будет продолжаться до тех пор
# пока не будет введено целое число

while True:
    try:
        int_val=int(input('Введите целое число: '))
        print(f'Вы успешно ввели целое число : {int_val}')
        break
    except ValueError: #ошибка  вначении
        print('Вас просят ввести целове число')
        print('Попробуйте снова')