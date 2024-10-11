# Обработчик изображений

from tkinter import *  # подключаем все элементы
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageEnhance


class App:
    def __init__(self):  # конструктор
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
        # кнопка загрузки
        self.btn = Button(text='Заменить', command=self.load)
        self.btn.pack(side=LEFT, anchor=N, padx=5, fill=X, expand=True)  # fill и expand  идуть только вместе рядом
        # кнопка размытия
        self.blur = Button(text='Размыть', command=self.blur)
        self.blur.pack(side=LEFT, anchor=N, padx=5, fill=X, expand=True)
        # кнопка резкость
        self.shrp = Button(text='Добавить резкость', command=self.sharp)
        self.shrp.pack(side=LEFT, anchor=N, padx=5, fill=X, expand=True)
        # кнопка отражения по горизонтали
        self.flp = Button(text='Отразить', command=self.flip)
        self.flp.pack(side=LEFT, anchor=N, padx=5, fill=X, expand=True)
        # кнопка возврата к оригиналу
        self.orig = Button(text='Оригинал', command=self.back)
        self.orig.pack(side=LEFT, anchor=N, padx=5, fill=X, expand=True)
        # Кнопка очистки
        self.rect_btn = Button(text='Очистить', command=self.make_rect)
        self.rect_btn.pack(side=LEFT, anchor=N, padx=5, fill=X, expand=True)# fill и expand  идуть только вместе рядом
        # Кнопка сохранения
        self.save_btn = Button(text='Сохранить', command=lambda: self.load_save('save')) #через lambda передаем весь объект с тем что ему сделать
        self.save_btn.pack(side=LEFT, anchor=N, padx=5, fill=X, expand=True)
        self.save_btn['state'] = DISABLED
        # self.btn.bind('<ButtonPress-1>', self.load)  # <ButtonPress-1> когда левая кнопка мыши, вызываем клик
        self.left, self.top = 0, 0  # точки привязки к холсту
        self.ext = ''  # расширение файла картинки
        self.image = None
        self.empty = Image.new('RGB', (600, 400), (255, 255, 255))  # пустышка
        self.root.mainloop()

    def load(self):
        try:
            fullpath = filedialog.askopenfilename(initialdir='./', filetypes=(
                ('All', '*.*'),
                ('JPEG', '*.jpg'),
                ('PNG', '*.png')
            ))  # диалог открытия картинки initialdir открывает там где корневая программа
            self.ext = fullpath.split('.')[-1]  # [-1] обращение к последнему эл списка, так вытащил расширение из пути
            # print(self.ext) проверить там расширение ли
            self.empty = Image.open(fullpath)
            mode = self.empty.mode  # получаем цветовую схему

            if mode == 'P':  # 256-color indexed image
                self.empty = self.empty.convert('RGB')  # конвертируем цветовую схему в rgb
            w, h = self.empty.size
            self.left, self.top = 0, 0

            if w > 600:  # если ширина больше ширы холста, то считаем соотношение ширины и
                ratio = w / 600  # посчитал соотношение ratio
                h = int(h / ratio)
                w = 600
                self.empty = self.empty.resize((600, h))
                if h < 400:
                    self.left, self.top = 0, (400 - h) // 2
                else:
                    self.left, self.top = 0, 0
            else:
                self.left = (600 - w) // 2
                self.top = (400 - h) // 2

            self.image = ImageTk.PhotoImage(self.empty)
            self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)

        except AttributeError:  # если не удалось подгрузить
            self.image = ImageTk.PhotoImage(self.empty)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    # def click(self, event):
    #     self.image = PhotoImage(file='images/logo.png')
    #     self.canvas.create_image(0, 50, anchor=NW, image=self.image)
    #     # self.btn['text']= 'Появилось изображение'
    #     # self.label['image']= self.image

    # Функционал кнопки размытия
    def blur(self):
        blur_img = self.empty.filter(ImageFilter.GaussianBlur(5))
        self.image = ImageTk.PhotoImage(blur_img)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        self.save_btn['state'] = NORMAL

    # Функционал кнопки резкости
    def sharp(self):
        sharper = ImageEnhance.Sharpness(self.empty)
        sharp_img = sharper.enhance(2.0)
        self.image = ImageTk.PhotoImage(sharp_img)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        self.save_btn['state'] = NORMAL

    # Функционал кнопки отражения
    def flip(self):
        flp_img = self.empty.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        self.image = ImageTk.PhotoImage(flp_img)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        self.save_btn['state'] = NORMAL

    # Функционал кнопки возврата к оригиналу
    def back(self):
        self.image = ImageTk.PhotoImage(self.empty)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        self.save_btn['state'] = DISABLED

    # Функционал кнопки сохранить
    def load_save(self, *args):
        if len(args) == 1 and args[0] == 'save':
            # print(args[0])
            fullpath = filedialog.asksaveasfilename(initialfile=f'result.{self.ext}')
            if fullpath != '':
                if f'.{self.ext}' not in fullpath:
                    fullpath += f'.{self.ext}'
                res = ImageTk.getimage(self.image)
                if res.mode == 'RGBA' and 'jp' in self.ext:
                    res = res.convert('RGB')
                res.save(fullpath)
                self.save_btn['state'] = DISABLED


    # Функционал кнопки "Очистить"
    def make_rect(self):
        self.canvas.create_rectangle(0, 0, 600, 400, fill='#ffffff')


app = App()
