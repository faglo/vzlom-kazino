from tkinter import *
from tkinter.ttk import Progressbar, Style
import webbrowser

window = Tk()
window.title("Взлом КАЗИНО")
Label(window, text="Казино взломано на 14%").pack(side='top')
Label(window, text="Выкачано 12 050 руб. из 70 055 020 руб.").pack()
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
        window.update()
        if i == 100:
            webbrowser.open("https://www.youtube.com/watch?v=vTUP8eimDuY")


Button(window, text="Да", command=on_click).pack(side='left')
Button(window, text="Нет").pack(side='right')
window.iconbitmap("777.ico")
window.mainloop()
