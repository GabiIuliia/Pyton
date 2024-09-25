# Сложное условие (логическое "И")


string = ''  # пустая строка
name = input('Как Вас зовут?')
surname = input('Ваша фамилия?')
age = input('Ваш возраст')
gender = input('Укажите пол (м или ж):')

if name == 'Вася' and surname == 'Пупкин':
    print('Уважайте Ваше имя!!!')
else:

    # основное условие
    if (gender == 'м' or gender == 'М' or
            gender == 'v' or gender == 'V'):
        string = 'Уважаемый'
    elif (gender == 'Ж' or gender == 'ж' or
          gender == ';' or gender == ':'):
        string = 'Уважаемый'
    else:
        string = 'Уважаемый товарищ'

    string = (string + name + '' + surname + ''
              + ' Ваш возраст: ' + age + '.')
    print(string)
