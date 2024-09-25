#Отрицание (или инверсия)
# Приоритет логических операторов
#1. not
#2. and
#3. or

flag=True #булева переменная
if flag:
    print('Включено')
else:
    print('Выключено')

print('Нажали кнопку')
flag=not flag #инвертирует flag и переприсвоит

if flag:
    print('Включено')
else:
    print('Выключено')