#Списки
#
#
from array import array

s={'',}#множество
empty_set=set()
array=[]#пустой список
array=list()#пустой список

#index    0       1        2
array=['ясно','пасмурно', 36.6] #36.6 не  итерируемый объект, '36.6'- строка итерируемый
okroshka=['огурец','картошка','колбаса','квас','соль']
print(okroshka[::2]) # чтобы не считать где конец len(okroshka) [0:len(okroshka):2]


#Поменять букву в слове. Строка является не изменяемым объектом
word='pithon' #immutable
lst=list(word) #превратили строку в список символов, и список можно менять
lst[1]='y'
print(*lst, sep='')  #* сообщает принту, что эта переменная список

dishes=['борщ','салат','пюре','котлета',]
#first, second, third=dishes распаковать список dishes
lanch,*dinner=dishes #распаковать список dishes где 1 относится к обеду и * список для ужина
print()

print(array[2])