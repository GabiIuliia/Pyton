# Файлы запись
# бывают текстовые или бинарные (двоичные)
# режимы : r-read, w- write, a-append
# Подрежим: b-binary, t-text

fo= open('sample.txt', 'wt+', encoding='UTF-8') # по умолчанию режим rt

print(fo.name, fo.mode, fo.encoding)
num=fo.write('Это текст внутри файла')

fo.close()

def f_open(name:str) -> str:
    #local score
    """
    читает текстовый файл и возвращает его содержимое
    :param name: имя файла на чтение
    :return: содержимое файла
    """
    with open (name, encoding='UTF-8') as f:

    return f.read()
res=f_open('sample.txt')
