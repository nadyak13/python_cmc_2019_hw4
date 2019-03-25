#!/usr/bin/env python3

import random
from tkinter import *

def get_colours():
    rgb_file = open('./rgb.txt', 'r')
    res = []
    for line in rgb_file:
        fields = line.split('\t')
        if fields[2].replace('\n', "") is not "":
            res += [fields[2].replace('\n', "")]
    return res

def update_color():
    global root, Txt
    idx = random.randint(0, len(colours) - 1)
    Txt['bg'] = colours[idx]
    idx = random.randint(0, len(colours) - 1)
    Txt['fg'] = colours[idx]

def add_two_elems():
    global root
    Butt.grid(row=1, column=0, sticky=E+W+S+N)
    Txt.grid(row=1, column=1, columnspan=2, sticky=E+W+S+N)

colours = get_colours()

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

Txt = Label(root, text="Label", bg="PeachPuff")
Butt = Button(root, text="Button", command=update_color)

TKroot.mainloop()
print("Done")
#root.destroy()
