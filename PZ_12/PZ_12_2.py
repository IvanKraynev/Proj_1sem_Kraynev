# Даны два числа. Вывести большее из них.

from tkinter import *

def num(event):
    a = int(num1.get())
    b = int(num2.get())
    if a > b:
        plus["text"] = "Первое число больше"
    if a < b:
        plus["text"] = "Второе число больше"

root = Tk()
root.title("Поиск большего числа")
root.geometry("300x100")

Label(text="Первое число:").grid(row=1, column=0)
num1 = Entry()
num1.grid(row=1, column=1)

Label(text="Второе число:").grid(row=2, column=0)
num2 = Entry()
num2.grid(row=2, column=1)

button1 = Button(text="Узнать результат")
button1.grid(row=4, column=1)

plus = Label()
plus.grid(row=5, column=1)
button1.bind("<Button-1>", num)
root.mainloop()