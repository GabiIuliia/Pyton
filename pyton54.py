# Область видимости преременных
#
# Глобальные рамки действия  global scope
b=5

def calс(x: int = 1, y: int = 0) -> int:
    #local score
    a=3
    res = 2 * x + y+ a
    return res


def multy(*args:int) -> int:
    """
    Функция вычисления произведения переменного числа аргументов
    :param args: ноль или несколько целых
    :return:  произведение аргументов
    """
    if len(args) == 0:
        return 0
    if len(args) ==1:
        return args
    res=1
    for i in range(len(args)):
        res *= args [0]
    return res


def increment():
    global b
    b +=1

print(multy(1,2,5,8))
increment()
result = calс(b)
#garbage collector (can)- сборщик  мусора
print(result)
