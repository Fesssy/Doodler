from tkinter import *

import fileOperations
import homeWindow
from gameLogic import *
from fileOperations import *


class drawing:
    def __init__(self, points=None, name=None):

        # creating root

        self.root = Tk()
        self.root.title("Draw")
        self.root.geometry("900x550")

        # initializing 'saved' variable
        self.saved = 0
        self.toDraw = True

        # creating frame
        rootFrame1 = Frame(self.root, height=550, width=200)
        rootFrame2 = Frame(self.root, height=550, width=500)
        rootFrame3 = Frame(self.root, height=550, width=200)

        rootFrame1.grid(column=1, row=1)
        rootFrame2.grid(column=2, row=1)
        rootFrame3.grid(column=3, row=1)

        # creating labels
        lab1 = Label(rootFrame1, text="Instructions")

        lab21 = Label(rootFrame1, text="arrows ->")
        lab22 = Label(rootFrame1, text="Traverse")

        lab31 = Label(rootFrame1, text="Tab ->")
        lab32 = Label(rootFrame1, text="Draw")

        lab41 = Label(rootFrame1, text="Color ->")
        lab42 = Label(rootFrame1, text="Red")

        lab51 = Label(rootFrame1, text="'R' ->")
        lab52 = Label(rootFrame1, text="Red")

        lab61 = Label(rootFrame1, text="'G' ->")
        lab62 = Label(rootFrame1, text="Green")

        lab71 = Label(rootFrame1, text="'B' ->")
        lab72 = Label(rootFrame1, text="Blue")

        # creating canvas
        self.canvas = Canvas(rootFrame2, height=500, width=500, bg="white", highlightcolor="#0080ff", highlightthickness=2)

        # creating drawing class object and declaring few variables
        if points is None:
            self.draw = Draw()
        else:
            self.draw = Draw(points)
            fileOperations.savetmp(name[:-4])
            self.saved = 1
            for x, y, z in points:
                self.canvas.create_text(x, y, text='●', fill=z)

        # initializing variables and objects to be used
        self.color = 'Black'
        self.a = self.canvas.create_text(250, 250, text='○', fill=self.color)


        # creating button
        btn1 = Button(rootFrame3, text="Cancel", command=self.cancel, bg="white", fg="black", bd=2, activebackground="#0080ff", activeforeground="white", height=1, width=12, font="Britannic 18 bold")
        btn2 = Button(rootFrame3, text="Save", command=self.Save, bg="white", fg="black", bd=2, activebackground="#0080ff", activeforeground="white", height=1, width=12, font="Britannic 18 bold")

        # binding the buttons and keys to functions
        self.root.bind('<Left>', self.move)
        self.root.bind('<Right>', self.move)
        self.root.bind('<Up>', self.move)
        self.root.bind('<Down>', self.move)
        self.root.bind('<space>', self.change_todraw)
        self.root.bind('<KeyPress>', self.change)

        # placing every object
        lab1.grid(column=1, row=1, columnspan=2)
        lab21.grid(column=1, row=2, rowspan=1)
        lab22.grid(column=2, row=2, rowspan=1)
        lab31.grid(column=1, row=3, rowspan=1)
        lab32.grid(column=2, row=3, rowspan=1)
        lab41.grid(column=1, row=4, rowspan=1)
        lab42.grid(column=2, row=4, rowspan=1)
        lab51.grid(column=1, row=5, rowspan=1)
        lab52.grid(column=2, row=5, rowspan=1)
        lab61.grid(column=1, row=6, rowspan=1)
        lab62.grid(column=2, row=6, rowspan=1)
        lab71.grid(column=1, row=7, rowspan=1)
        lab72.grid(column=2, row=7, rowspan=1)

        btn1.grid(column=1, row=1, ipadx=5, ipady=5, padx=5, pady=5)
        btn2.grid(column=1, row=2, ipadx=5, ipady=5, padx=5, pady=5)

        self.canvas.pack(fill="both", expand=True)

        # starting loop
        self.root.after(1000, self.warn)
        self.root.mainloop()

    def move(self, event):
        self.draw.movement(event.keysym, self.color, self.toDraw)
        self.canvas.move(self.a, self.draw.getX(), self.draw.getY())
        if self.toDraw:
            (x, y) = (self.draw.getPointerX(), self.draw.getPointerY())
            self.canvas.create_text(x, y, text='●', fill=self.color)

    def change(self, event):
        switcher = {'r': 'Red', 'g': 'Green', 'b': 'Blue'}
        self.color = switcher.get(event.char, 'black')

    def Save(self):
        saveFile(str(self.draw.getPaint()), self.saved)
        self.saved = 1

    def cancel(self):
        self.root.destroy()
        homeWindow.main()

    def change_todraw(self, event):
        self.toDraw = not self.toDraw

    def warn(self):
        messagebox.showwarning("Warning", "You cannot 'UNDO' or 'ERASE' here !!!")


def main():
    drawing()


def main2(pointers, fname):
    drawing(pointers, fname)
