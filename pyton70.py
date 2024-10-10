# Обработчик изображений

from tkinter import * # подключаем все элементы

from pyton1 import sides


class App:
    def __init__(self):
        self.root=Tk() # корневой элемент
        self.root.title('Обработка изображений')
        self.root.geometry('800x600') #размеры окна
        self.root.resizable(True,False) # фиксируем габариты
        self.root.iconphoto(False, PhotoImage(file='images/convert.png')) #True только для этого окна False для всех окон
        self.label=Label(text='Работаем с картинками и изображениями', background='#ffff00', foreground='#ffaa00', font=('Verdana', 16))
        self.label.pack()  # примитивный способ размещения -размещение ярлыка или надписи посередине во всю ширину
        self.canvas=Canvas(bg='while', width=600,height=400)
        self.canvas.pack(ancore=CENTER , pady=20) #pady отвечает за отступы y у pad сверху и снизу, padx x по бокам
        self.btn=Button(text='Заменить')
        self.btn.pack(side=LEFT,  ancor=N, padx=25, fill=X, expand=True) # fill и expand  идуть только вместе рядом
        self.rect_btn=Button(text='Покажись')
        self.rect_btn.pack(side=LEFT,  ancor=N, padx=25, fill=X, expand=True) # fill и expand  идуть только вместе рядом
        self.btn.bind('<ButtonPress-1>', self.click) # <ButtonPress-1> когда левая кнопка мыши, вызываем клик
        self.image= None
        self.root.mainloop ()


    def click (self, event):
        self.image=PhotoImage(file='images/logo.png')
        self.canvas.create_image(0,50, ancor=NW, image=self.image)
        # self.btn['text']= 'Появилось изображение'
        # self.label['image']= self.image


app=App()