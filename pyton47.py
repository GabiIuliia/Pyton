# Файлы чтение
# бывают текстовые или бинарные (двоичные)
# режимы : r-read, w- write, a-append
# Подрежим: b-binary, t-text
from operator import index

fo= open('sample.txt', 'rt', encoding='UTF-8') # по умолчанию режим rt
print(fo.name, fo.mode, fo.encoding)
# fo.read(10)
# text=fo.read(6)
# print(text)
text=fo.read()
fo.close()

#как извлечь нужный фрагмент из текста
lst=text.split()
# способ 1
if 'внутри' in lst:
    for word in lst:
        if word == 'внутри':
            print(word)
else:
    print('Такого слова в файле нет')


#способ 2

if 'внутри' in lst:
    index= lst.index('внутри') #метод списка индекс
        print(lst[index])
else:
    print('Такого слова в файле нет')



"""
d = {
    'стул': 'chair',
    'стол': 'table',
    'яблоко': 'apple', #висячая запятая
}

rus =input('Введите слово на русском для перевода (или "стоп" для выхода): ').strip().lower()
while rus != 'стоп' and rus != 'cnjg':

    if rus in d:
        print(f'Слово {rus} переводится как {d[rus]}')
    else:
        print(f'К сожалению я не знаю слово {rus}')
        new_word=input(f'А как слово {rus} переводится:')
        d[rus]= new_word
        print(f'Теперь я знаю перевод слова {rus} это {d[rus]}')

print('Возвращайтесь к нам')"""