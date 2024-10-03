#Функции- антонимы chr и ord
# ASCII (256 вариантов знаков)- 8бит (2^8)
# Unicode (65536 вариантов знаков)- 16 бит (2^16)

# print(ord('a'))
# print(chr(97))

print(ord ('»'))
print(f'{chr(171)}HELLO{chr(187)}')
print(chr(10000))


print('75'+chr(176)+'C')
print(f'75{chr(176)}C')
print('75\xB0C')
print('\u2710')

temp=s.digits+s.assii_lowercase+s.assii_uppercase
m_set=set(temp)-{'l','O','0','I','1','M'}
print(temp)