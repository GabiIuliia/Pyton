

def divide():
    a=input('Введите а: ')
    b=input('Введите b: ')
    try:
        temp=float(a)/float(b)
        return temp
    except ZeroDivisionError:
        return 'Не делите на 0'
    except ValueError:
        return 'Нужно вводить целое число '
    return a/b


print(divide())