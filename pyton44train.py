# упражнение- справочная вокзаа


trains = {
    '001A': ['"Красная стрела"', 'Москва-СПБ', '23:55'],
    '002B': ['"Смена"', 'Москва-СПБ', '20:40'],
    '003C': ['"Алегро"', 'Воронеж-СПБ', '15:30'],
}
while True:
    num = input('Введите номер поезда (или "стоп" для выхода): ').strip().upper() #все что пользователь вводит переводит в большие буквы и сравнивает с этим
    if num == 'СТОП' or num == 'CNJG':
        print('Возвращайтесь к нам')
        break

    if num not in trains:
        print('Такого номера нет. Выберете из списка ниже: ')
        for k, v in trains.items():
            print(f'{k}-{v[1]}')
    else:
        print(f'Поезд {num}{trains[num][0]} маршрут: {trains[num][1]}.'
              f'Отправляется  в {trains[num][2]}')
