# Подстрок к списку и наоборот

okroshka = ['огурец', 'картошка', 'колбаса', 'квас', 'соль']
additional = ['редис', 'перец']
a = okroshka + additional

b = a[:3]  # делаем срез
b.sort()  # сортировали
# вывод списка строкой (способ №1)
print(*b, sep=',')
# вывод списка строкой (способ №2 з списка в строку) join-метод строки, канкотенирует строки , соединяет интерируемые объекты
result = ','.join(b)
print(result)

#Строковый метод
word = 'Pithon'
lst = list(word)
lst[1] = 'y'
result = ''.join(lst)
print(result)
