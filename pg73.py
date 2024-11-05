# списочные выражения (list comprehensions)
# [ выражение for переменная in источник if условие]

# a= list (range (1,11)

# a= []
# for i in range (1,11):
# a.append (i)

# a = [i for i in range(1, 11)]  # список
# a = [i * i for i in range(1, 11)]  # список в квадрате
# print(a)

ipaddress = '192.168.0.1'
# s = ipaddress.split('.')
# a= map (int,s)
# print(s)
a = [int(i) for i in ipaddress.split('.') if int(i) > 0]
print(a)

b = [i for i in range(2, 11, 2)]
print(b)

d= 'Только Большие Буквы'
c = [i for i in d if i.isupper()]
print(c)
e=[(pos,char) for pos, char in enumerate (d)]
print(e)

