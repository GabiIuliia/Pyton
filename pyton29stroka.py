# основные методы строки


s='Язык Pythonnnn'

print(s.lower()) #все буквы маленькие
print(s.upper()) #все буквы большие
print(s.capitalize()) #все буквы как в предложениях (начинается с большой и далее маленькие)
print(s.title())#все слова будут начинаться с большой буквы
print(s.strip('я')) #раздевает строку, снимает с строки левый lstrip или правый символ rstrip,
# если ничего не указать удаляет все пробеы
# в начале и все пробелы в конце
print(s.count('n')) #поиск в строке
print(s.index('')) #поиск в строке первый индекс в строке
print(s.find('')) #индекс вхождения
print(s.replace('')) #замена значений (замена подстроки с указанием количества)
print(s.startswith('Язык')) #начинается ли с



s=input('Введите:').strip().lower()

poli= s[::-1]

if poli == s:
    print('Вы ввели полиндром', s,'-','палиндром')
else:
    print('обычное слово')