#!/usr/bin/env python3

from tkinter import *

def add_two_elems():
    Txt = Label(root, text="Label", bg="PeachPuff")
    Txt.grid(row=1, column=1, columnspan=2, sticky=E+W+S+N)
    Butt = Button(root, text="Button")
    Butt.grid(row=1, column=0, sticky=E+W+S+N)

TKroot = Tk()
TKroot.title("Hello")

root = Frame(TKroot)
root.place(relx=0, rely=0, relheight=1, relwidth=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(0, weight=10)
root.rowconfigure(1, weight=1)

Add = Button(root, text="Add", command=add_two_elems)
Add.grid(row=0, column=0, sticky=E+W+S+N)
Exit = Button(root, text="Exit", command=root.quit)
Exit.grid(row=0, column=1, sticky=E+W+S+N)

TKroot.mainloop()
print("Done")
#root.destroy()
