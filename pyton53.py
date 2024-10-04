# Функция (encapsulation- инкапсуляция)
# Описание define функции


def odd_even(num:int)-> str:
    """
    Функция возвращает чет или нечет
    :param num: целое число
    :return: строку в которой чет или нечет
    """
    if not isinstance(num, int):
        return 'Проверить можно только целое число'
    if num % 2:
        return 'нечет'
    return 'чет'

# вызов
res=odd_even(11000)
print(res)