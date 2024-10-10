# Обработчик изображений

from tkinter import *  # подключаем все элементы
from tkinter import filedialog
from PIL import Image, ImageTk


class App:
    def __init__(self):
        self.root = Tk()  # корневой элемент
        self.root.title('Обработка изображений')
        self.root.geometry('800x600')  # размеры окна
        self.root.resizable(True, False)  # фиксируем габариты
        self.root.iconphoto(False,
                            PhotoImage(file='images/convert.png'))  # True только для этого окна False для всех окон
        self.label = Label(text='Работаем с картинками и изображениями', background='#ffff00', foreground='#ffaa00',
                           font=('Verdana', 16))
        self.label.pack()  # примитивный способ размещения -размещение ярлыка или надписи посередине во всю ширину
        self.canvas = Canvas(bg='white', width=600, height=400)
        self.canvas.pack(anchor=CENTER, pady=20)  # pady отвечает за отступы y у pad сверху и снизу, padx x по бокам
        self.btn = Button(text='Заменить')
        self.btn.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)  # fill и expand  идуть только вместе рядом
        self.rect_btn = Button(text='Покажись', command=self.make_rect)
        self.rect_btn.pack(side=LEFT, anchor=N, padx=25, fill=X,
                           expand=True)  # fill и expand  идуть только вместе рядом
        self.btn.bind('<ButtonPress-1>', self.load)  # <ButtonPress-1> когда левая кнопка мыши, вызываем клик
        self.image = None
        self.empty = Image.new('RGB', (600, 400), (255, 255, 255))  # пустышка
        self.root.mainloop()

    def load(self, event):
        try:
            fullpath = filedialog.askopenfilename(initialdir='./', filetypes=(
                ('JPEG', '*.jpg'),
                ('PNG', '*.png')
            ))  # диалог открытия картинки initialdir открывает там где корневая программа
            self.empty = Image.open(fullpath)
            mode = self.empty.mode  # получаем цветовую схему
            if mode == 'P':  # 256-color indexed image
                self.empty = self.empty.convert('RGB')  # конвертируем цветовую схему в rgb
            w, h = self.empty.size
            if w > 600:  # если ширина больше ширы холста, то считаем соотношение ширины и
                ratio = w / 600  # посчитал соотношение ratio
                self.empty = self.empty.resize((600, int(h / ratio)))
            self.image = ImageTk.PhotoImage(self.empty)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)

        except AttributeError:  # если не удалось подгрузить
            self.image = ImageTk.PhotoImage(self.empty)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    # def click(self, event):
    #     self.image = PhotoImage(file='images/logo.png')
    #     self.canvas.create_image(0, 50, anchor=NW, image=self.image)
    #     # self.btn['text']= 'Появилось изображение'
    #     # self.label['image']= self.image

    def make_rect(self):
        self.canvas.create_rectangle(0, 0, 600, 400, outline='#000000', fill='#80CBC4', width=5)


app = App()
