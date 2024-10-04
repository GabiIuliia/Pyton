# Обучаемый словарь

# d = {
#     'стул': 'chair',
#     'стол': 'table',
#     'яблоко': 'apple',  # висячая запятая
# }

d={} #наполнять будем из файла dict.dat
with open('dict.dat', encoding='UTF-8') as fileone:
    line=fileone.readline().rstrip('\n')
    while line != '': # если строка существует
        k,v=line.split('|')
        d[k]=v
        line= fileone.readline().rstrip('\n')




rus = input('Введите слово на русском для перевода (или "стоп" для выхода): ').strip().lower()
while rus != 'стоп' and rus != 'cnjg':

    if rus in d:
        print(f'Слово {rus} переводится как {d[rus]}')
    else:
        print(f'К сожалению я не знаю слово {rus}')
        new_word = input(f'А как слово {rus} переводится:')
        d[rus] = new_word
        print(f'Теперь я знаю перевод слова {rus} это {d[rus]}')
    rus = input('Введите слово на русском для перевода (или "стоп" для выхода): ').strip().lower()

# менджер контекста (файл закрывается автоматически)
with open('dict.dat', 'wt', encoding='UTF-8') as fileone:
    for k, v in d.items():
        print(k, v, sep = '|', file=fileone)

    # Или такой способ, но нужно не забыть закрыть строчку
    # file= open('dict.dat', 'wt+', encoding='UTF-8')
    # file.close()

print('Возвращайтесь к нам')
