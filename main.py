import tkinter as tk
from tkinter import ttk
import settings

class Application:
    def __init__(self):
        self.width = settings.width
        self.height = settings.height

        self.app = tk.Tk() #Создание окна приложения
        self.app.title(settings.title)
        self.app.configure(bg=settings.color)

    def draw_element(self):

        #Текст
        self.lbl_head = tk.Label(text="IMT", bg=settings.color_button, width=15, height=2, fg="white")
        self.lbl_head.pack(pady=20, padx=20)

        #Поля ввода -Entry
        self.label_text_entry_1 = tk.Label(text="Введите ваш рост", fg="black", bg=settings.color, width=15, height=2)
        self.label_text_entry_1.place(x=95, y=83)

        self.entry_1 = tk.Entry(fg="black", bg="white", width=30, borderwidth=0)
        self.entry_1.place(x=100, y=113)


        self.label_text_entry_2 = tk.Label(text="Ваш вес", fg="black", bg=settings.color, width=15, height=2)
        self.label_text_entry_2.place(x=70, y=153)

        self.entry_2 = tk.Entry(fg="black", bg="white", width=30, borderwidth=0)
        self.entry_2.place(x=100, y=183)

        #Кнопка вычисления
        self.button_result = tk.Button(text="Узнать", fg="white", bg=settings.color_button, width=20, height=2)
        self.button_result.pack(pady=150)
        #Установка реакции
        self.button_result.bind("<Button-1>", self.reaction_click_button)

        #Кнопка очистки
        self.button_clear = tk.Button(text="Очистить", fg="white", bg=settings.color_button, width=20, height=2)
        self.button_clear.place(x=125, y=280)
        self.button_clear.bind("<Button-1>", self.reaction_click_clear_button)
    def display(self):
        self.draw_element()
        self.centerWindow()
        self.app.mainloop() #Запуск приложения

    def centerWindow(self):
        #Размер экрана
        w, h = settings.width, settings.height

        #Узнаём размер ширины и высоты приложения
        w_width = self.app.winfo_screenwidth()
        w_heigth = self.app.winfo_screenheight()

        #Определяем высоту и ширину экрана
        x = (w_width - w) / 2
        y = (w_heigth - h) / 2

        self.app.geometry("%dx%d+%d+%d"  % (w, h, x, y))

    def reaction_click_button(self, event):
        flag = False
        try:
            height = int(self.entry_1.get()) / 100
            weight = int(self.entry_2.get())
        except Exception:
            flag = True

        if flag == True:
            self.imt = "None"
        else:
            self.imt = round(weight / (height**2), 2)

        self.information = tk.Label(text="Ваш IMT: {}".format(self.imt), bg=settings.color_button, width=15, height=2, fg="white")
        self.information.place(x=145, y=330)

    def reaction_click_clear_button(self, event):
        try:
            self.information.destroy()
            self.entry_1.delete(0, tk.END)
            self.entry_2.delete(0, tk.END)
        except AttributeError:
            print("Error")

if "__main__" == __name__:
    app = Application()
    app.display()