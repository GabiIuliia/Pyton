#проверка строки на палиндром
s=input('Введите:')

poli= s[::-1]

if poli == s:
    print('Вы ввели полиндром', s,'-','палиндром')
else:
    print('обычное слово')
