# syntax sugar (синтаксический сахар)
печать = print  # передал ссылку на print

печать('Здравствуйте', 'До свидания', sep=' и ')

a = list(range(1, 11))  # list превращает то что генерирует range в список от 1 до 10

# Функция высшего порядка
b = list(map(str, a))  # функция map берет как объект и превращает в список строк или списком флоат ...
print(b)
res = ' и '.join(b)

print(res)


# сделать список квадратов чисел из исходного списка
def square(num):
    return num ** 2


# ll=lambda num: num ** 2 # говорим lambda вот входной параметр (num) а вот выходной т.е. что с этим делаем (num**2)
# summ=lambda a,b:a+b

sq = list(map(square, a))
print(sq)

fruits=['манго','ананас','банан','киви','клубника']
fruits.sort(key=lambda letter:letter[1])
print(fruits)
