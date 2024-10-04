# Файлы запись нескольуких строк в файл
# бывают текстовые или бинарные (двоичные)
# режимы : r-read, w- write, a-append
# Подрежим: b-binary, t-text
total=0
fo= open('sample.txt', 'at', encoding='UTF-8') # по умолчанию режим rt
fo.write('\n') #перевод на новую строку
num=fo.write('Это новая строка внутри файла\n')
total += num
num=fo.write('Это 2новая строка внутри файла\n')
total += num
print(f'В файл {fo.name} записано {total} байт или символов')
fo.close()
