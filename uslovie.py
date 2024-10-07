def sum(a, b):
    """
    Сумма 2 чисел
    :param a:
    :param b:
    :return:
    """
    try:
        a = float(a)
        b = float(b)
        res = a + b
    except TypeError:
        return 'Складываю числа'
    else:
        return res


def sub(a, b):
    """
    Разница 2 чисел
    :param a:
    :param b:
    :return: разность
    """
    try:
        a = float(a)
        b = float(b)
        res = a - b
    except TypeError:
        return 'Вычитаю числа'
    else:
        return res


def truediv(a, b):
    """
    Частное 2 чисел
    :param a:
    :param b:
    :return: деление
    """
    try:
        a = float(a)
        b = float(b)
        res = a / b
    except TypeError:
        return 'Делю только числа'
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    else:
        return res


def multiply(a, b):
    """
    Произведение 2 чисел
    :param a:
    :param b:
    :return: умножение
    """
    try:
        a = float(a)
        b = float(b)
        res = a * b
    except TypeError:
        return 'Умножаю только числа'
    else:
        return res


