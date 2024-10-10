# GUI- Graphic user interface
# Библиотека с уроками PyQt6

import tkinter
from PIL import Image, ImageTk


class App:
    def __init__(self):
        # корневой элемент приложения
        self.root = tkinter.Tk()

        # рабочая область - frame рамка
        self.frame = tkinter.Frame(self.root)
        self.frame.grid()

        # Добавляем ярлык
        self.label = tkinter.Label(self.frame, text='Что-то').grid(row=1, column=1)

        # добавляем кнопку
        self.but = tkinter.Button(self.frame, text='Кнопка', command=self.change).grid(row=1, column=2)

        # добавляем холст
        self.canvas = tkinter.Canvas(self.root, height=369, width=1197)
        self.image = Image.open('images/logo.png')
        self.photo = ImageTk.PhotoImage(self.image)
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=2, column=1)

        self.root.mainloop()  # ожидание действий пользователя

    # добавляем метод change
    def change(self):
        print('кнопку нажали')
        self.image = Image.open('images/cont.png')
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=2, column=1)


app = App()
