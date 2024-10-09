# Доп. библиотека PIL (pillow)
from PIL import Image, ImageFilter,

# Пробуем прочитать файл logo.png

try:
    orig = Image.open('images/logo.png')
except FileNotFoundError:
    print('Файл не найден')

print('параметры считанного файла')
print(f'Формат :{orig.format}')
print(f'Размеры :{orig.size}')
print(f'Цветовая схема :{orig.mode}')

w, h = orig.size  # получили и распаковали кортеж
pixels = orig.load()  # список пикселей [x,y]

# pixels[171, 92] = (152,0,17)
# for x in range(w):
#     for y in range(h):
#         r, g, b = pixels[x, y]
#         average = (r, g, b)//3
#         pixels[x, y] = average, average, average
orig.save('image/zvet.png')

blur = orig.filter(ImageFilter.GaussianBlur(10))
cropped = orig.crop((171, 0, 1197, 92))
contour = orig.filter(ImageFilter.CONTOUR)

contour.save('images/cont.png')
cropped.save('images/crop.png')
blur.save('images/blur.png')
