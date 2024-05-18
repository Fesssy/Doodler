from tkinter.simpledialog import askstring
from tkinter import messagebox
import os

tmp = ""


def savetmp(name):
    global tmp
    filenm = "C:/Users/alien/OneDrive/Desktop/Python/savedDrawing/" + name + ".txt"
    tmp = filenm


def saveFile(data, saved):
    global tmp
    if not saved:
        try:
            name = askstring('File Name', 'Name of the File?')
        except:
            return
        savetmp(name)
        with open(tmp, 'w') as file:
            file.write(data)
    else:
        with open(tmp, 'w') as file:
            file.write(data)


def deleteFile(name):
    savetmp(name)
    res = messagebox.askyesno("Confirmation", "Are You sure?")
    if res:
        try:
            os.remove(tmp)
            messagebox.showinfo("Info", f"{name}"+" deleted successsfuly.")
        except:
            messagebox.showerror("Error", "While deleting the file some error occured, try again!")



def readfile(filename):
    with open(filename, 'r') as file:
        data = file.read()
        return data

