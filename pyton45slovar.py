#Обучаемый словарь

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

print('Возвращайтесь к нам')