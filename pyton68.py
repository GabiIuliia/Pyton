# Доп. библиотека PIL (pillow)
from PIL import ImageDraw, Image, ImageFont

"""
# создаем и рисуем
# 1 холст

canvas=Image.new ("RGB", (200,200), (128,128,128))

# создаем рисовальщик
draw=ImageDraw.Draw(canvas)


#рисуем линию
draw.line((0,0,200,200), fill=(255,0,0), width=3)

#рисуем прямоугольник
draw.rectangle((0,0,50,50), fill=(0,0,255))

#рисуем элипс
draw.ellipse((0,0,200,200), outline='brow', width=5)

# рисуем полигон (треугольник)
draw.polygon(
    xy=(
        (200,200),
        (150,200),
        (200,150)
    ), fill='orange', outline=(0,0,0)
)

#сохраняем
canvas.save('images/line.png', 'PNG')
"""


canvas=Image.new ("RGB", (200,200), (0,0,230))

# создаем рисовальщик
draw=ImageDraw.Draw(canvas)


#рисуем линию
draw.line((0,100,200,100), fill=(150,150,150), width=3)
draw.line((100,0,100,200), fill=(150,150,150), width=3)

#рисуем прямоугольник
draw.rectangle((0,0,200,200), outline=(100,100,100), width=6)

# напишем текст
text='Окно'
fon=ImageFont.truetype('arial.ttf', size=18)
draw.text((80,90), text, font=fon)

#сохраняем
canvas.save('images/line2.png', 'PNG')



