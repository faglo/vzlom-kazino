from tkinter import *
from tkinter.ttk import Progressbar, Style
import webbrowser
from math import floor

window = Tk()
window.title("Взлом КАЗИНО")
l1 = Label(window, text="Казино взломано на 14%")
l1.pack(side='top')
l2 = Label(window, text="Выкачано 12 050 руб. из 70 055 020 руб.")
l2.pack()
Label(window, text="Продолжить?").pack()
style = Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='red')
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 28
bar.pack()


def on_click():
    for i in range(28, 101):
        bar['value'] = i
        l1['text'] = "Казино взломано на {}%".format(i)
        l2['text'] = "Выкачано {} руб. из {} руб.".format(
            floor(i * 70552020/100), 70552020)
        window.update()
        if i == 100:
            l1['text'] = "Казино взломано на {}%".format("159 УК РФ")
            webbrowser.open("https://www.youtube.com/watch?v=vTUP8eimDuY")


Button(window, text="Да", command=on_click).pack(side='left')
Button(window, text="Нет").pack(side='right')
window.iconbitmap("777.ico")
window.mainloop()
