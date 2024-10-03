#манипуляции со списком. операции со списком и методы списков



okroshka=['огурец','картошка','колбаса','квас','соль']
additional=['редис', 'перец']
final=okroshka +additional

#Способ 1
""" print(final+['петрушка'])#
print('Ингридиентов в окрошке', len(final))
print('Вот они')
count=1
for item in final:
    print(f'\t{count}.{item}')
    count+=1
# for item in final:
#     print(item)"""

# Способ 2
print('Ингридиентов в окрошке', len(final))
print('Вот они')
final.sort()
for item in range(len(final)):
    print(f'\t{item+1}.{final[item]}')

# Способ 3 (не использовать цикл и count+1)
print(*final)

