from tkinter import *
from tkinter import ttk
import drawingWindow as dw
import os
import ast

import fileOperations


class win():
    def __init__(self):
        self.root = Tk()
        self.root.title("Drawings")
        self.root.geometry("520x550")

        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=True)

        self.main_canvas = Canvas(self.main_frame)
        self.main_canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.main_frame, orient='vertical', command=self.main_canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.main_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.main_canvas.bind('<Configure>', lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all")))

        self.second_frame = Frame(self.main_canvas)
        self.main_canvas.create_window((0, 0), window=self.second_frame, anchor='nw')

        self.showdrawing()
        self.root.mainloop()

    def showdrawing(self):
        self.counter = 0
        self.data = None
        self.name = None
        dir_path = "C:/Users/alien/OneDrive/Desktop/Python/savedDrawing"

        for path in os.listdir(dir_path):

            filename = os.path.join(dir_path, path)

            if os.path.isfile(filename):
                self.name = os.path.basename(filename)
                self.counter += 1

                with open(filename, 'r') as file:
                    self.data = ast.literal_eval(file.read())

                self.frame = Frame(self.second_frame)
                self.canvas = Canvas(self.frame, height=500, width=500, bg="white", highlightcolor="#0080ff", highlightthickness=2, highlightbackground="#0080ff")
                self.btn = Button(self.frame, text=self.name[:-4], command=lambda value=self.data, fname=self.name: self.edit(value, fname), bg="white", fg="black", bd=2, activebackground="#0080ff", activeforeground="white", height=1, width=12, font="Britannic 18 bold")
                self.btn2 = Button(self.frame, text="Delete", command=lambda fname=self.name[:-4]: self.delete(fname), bg="white", fg="black", bd=2, activebackground="#0080ff", activeforeground="white", height=1, width=12, font="Britannic 18 bold")

                for x, y, z in self.data:
                    self.canvas.create_text(x, y, text='●', fill=z)

                self.frame.pack()
                self.canvas.pack()
                self.btn.pack()
                self.btn2.pack()


    def edit(self, points, name):
        self.root.destroy()
        dw.main2(points, name)

    def delete(self, name):
        fileOperations.deleteFile(name)
        self.root.destroy()
        self.__init__()


def main():
    win()
