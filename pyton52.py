# Функция (encapsulation- инкапсуляция)
# Описание define функции


def say_hello(name='noname', surname='nos'):
    """
    Функция приветствия
    :param name: имя, с которым здороваются
    :param surname:
    :return:
    """


    print('hello', name, surname)


# вызов
print(say_hello())
say_hello('Дмитрий')