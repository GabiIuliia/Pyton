# Файлы запись
# бывают текстовые или бинарные (двоичные)
# режимы : r-read, w- write, a-append
# Подрежим: b-binary, t-text

fo= open('sample.txt', 'wt+', encoding='UTF-8') # по умолчанию режим rt

print(fo.name, fo.mode, fo.encoding)
num=fo.write('Это текст внутри файла')

fo.close()

