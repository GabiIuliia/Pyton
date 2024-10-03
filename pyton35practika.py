
import string as s
import random as r #(перемешать)
#выбрали количество символов, которое будет в пароле
num=8
#Набор для пароля из букв и цифр
set_of_symbols= s.digits+s.ascii_lowercase+s.ascii_uppercase
#Превращаем в множество
set of symbol=set(set_of_symbols) #преобразовали в множество (множестов не упорядоченная коллекция,поэтому все перемешалось)
#удаляем сомнительные символы
set_of_symbols=set_of_symbols-{'l','O','0','I','1','M'} #убрали символы
#множество больше не нужно, превращаем в список
set_of_symbols=list(set_of_symbols)
#замешали полученный список
r.shuffle (set_of_symbols)
#берем первые num символов
temp=set_of_symbols[:num]
temp+=['@','!', '#','$'] #добавили спец символы
r.shuffle(temp) #замешали спец символы со всеми
#объединяем все символы из спикса в одну строку
password=''.join(temp)
#выводим результат
print(set_of_symbols)