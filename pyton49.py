fo= open('sample.txt', 'wt+', encoding='UTF-8')

print(dir(fo))

text=fo.readline()
while text != '':
print(text, and '')
text=fo.readline()