#Словари
# d=dickt () #пустой словарь
# d={} # пустой словарь


d = {
    'стул': 'chair',
    'стол': 'table',
    'яблоко': 'apple'
    ' меню': ['суп','тефтели', 'чай'], #висячая запятая
}

# print(d['стул'] [0])
d['слива']='plum'
d[0]='опе'
d[36.6]='normal'
d[true]='истина'
# print(d[true])
print(len(d)) #
print(list(d.keys())) #
print(list(d.values())) #
print(list(d.items())) #
# если слива есть в
if 'слива' in d.keys():
    print('Слива есть среди ключей')
#  если истина есть в
if 'истина' in d.values():
    print('слово истина есть среди ключей')
#
for key, value in d.items():
    if value=='истина':
        print(f'Для слова истина ключ- {key}')
#
for key in d:
    print(f'Ключ: {key}, Значение: {d[key]}')
#мягко обратиться к словарю, и будет не ошибка а присвоится к этому значению-0 (т.е. если значения нет, то ввыводит то что мы назначим - к примеру 0)
print(d.get('груша'))
# говорим del какой словарь и какой ключ
del d ['груша']

