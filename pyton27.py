# index 012345- порядковый номер элемента в последовательности
# slice-срез [start:stop:step]
s = 'python'

print(s[::-1]) #разворот строки срезом
length = len(s)  # для индекса отнимаем единицу
print('Длина строки', s, length)

for ch in s:
    print(ch)
