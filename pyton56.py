# Обработка исключений
# try (начало обработки)
# здесь выполяется "попытка" какого-либо действия
# exept (сама обработка)
# исключение обрабатывается
# finally (не  обязательная )
# программа продолжается с этого места,
# независимо от того, было исключение или нет
# else
# если не было исключения


def divide():
    a=input('Введите а: ')
    b=input('Введите b: ')
    try:
        temp=int(a)/int(b)
        return temp
    except ZeroDivisionError:
        return 'Не делите на 0'
    # except Exception as exp:
    #     return  f'Вот такая ошибка: {exp.}'
    except ValueError:
        return 'Нужно вводить целое число '
    return a/b


print(divide())


def divide():
    a=input('Введите а: ')
    b=input('Введите b: ')
    try:
        temp=int(a)/int(b)
        return temp
    except ZeroDivisionError:
        return 'Не делите на 0'
    # except Exception as exp:
    #     return  f'Вот такая ошибка: {exp.}'
    except ValueError:
        return 'Нужно вводить целое число '
    return a/b


print(divide())