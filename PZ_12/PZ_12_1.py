# Вариант 22

from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
root = Tk()
root.title('Security Realm')
root.geometry('900x570')
Label(root, text='Active Directory', font='Arial 11').place(x=27,y=0)
Label(root, text='Domains',font='Arial 11').place(x=10,y=35)
Label(root, text='Domain Name', font='Arial 11').place(x=250,y=55)
Entry(width=60, font='Arial 11').place(x=370,y=60)
Label(root, text='Domain controller', font='Arial 11').place(x=250,y=90)
Entry(width=60, font='Arial 11').place(x=370,y=92)
Button(root, text='Delete Domain', font='Arial 10 bold', bg='papaya whip').place(x=775,y=120)
Button(text='Add Domain', font='Arial 10 bold', bg='papaya whip').place(x=235,y=140)
Label(root, text='Site',font='Arial 11').place(x=10,y=180)
Entry(width=80, font='Arial 11').place(x=235,y=182)
Label(root, text='Bind DN',font='Arial 11').place(x=10,y=220)
Entry(width=80, font='Arial 11').place(x=235,y=222)
Label(root, text='Bind Password',font='Arial 11').place(x=10,y=260)
Entry(width=80, font='Arial 11').place(x=235,y=262)
Label(root, text='Group Membership Lookup Strategy',font='Arial 10').place(x=10,y=300)
combo = Combobox(root)
combo['values'] = ('Automatic','Manual')
combo.current()
combo.place(x=235,y=300)
Label(root, text='Remove irrelevant groups ',font='Arial 11').place(x=10,y=340)
var1 = IntVar()
check1 = Checkbutton(root, variable = var1, onvalue = 1,offvalue=0)
check1.place(x=235,y=340)
Label(root, text='Enable cache ',font='Arial 11').place(x=10,y=380)
var2 = IntVar()
check2 = Checkbutton(root, variable = var2, onvalue = 1,offvalue=0)
check2.place(x=235,y=380)
Label(root, text='Enviroment Properties ',font='Arial 11').place(x=10,y=420)
Button(text='Add', font='Arial 10 bold', bg='papaya whip').place(x=235,y=420)
Label(root, text='Test Domain Name ',font='Arial 11').place(x=10,y=460)
Entry(width=80, font='Arial 11').place(x=235,y=464)
Label(root, text='Test Domain Controllers ',font='Arial 11').place(x=10,y=500)
Entry(width=80, font='Arial 11').place(x=235,y=504)
Label(root, text='Success ',font='Arial 11').place(x=235,y=540)
Button(text='Test a test Domain', font='Arial 10 bold', bg='papaya whip').place(x=765,y=540)
root.mainloop()
