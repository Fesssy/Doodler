from tkinter import *
from PIL import Image, ImageTk
import drawingWindow
import showDrawingWindow


class home:

    # setting the root window
    def __init__(self):
        self.root = Tk()
        self.root.title("DOODLER")
        self.root.geometry("720x580")
        self.root.resizable(width=False, height=False)

        # loading image and converting to PhotoImage
        img = Image.open("C:/Users/alien/Downloads/cover.gif")
        img = img.resize((700, 500))
        img = ImageTk.PhotoImage(img)

        speakerImg = Image.open("C:/Users/alien/Downloads/speaker-filled-audio-tool.png")
        speakerImg = speakerImg.resize((50, 50))
        speakerImg = ImageTk.PhotoImage(speakerImg)

        # creating label for title
        title=Label(self.root, text="Doodler", font="Forte 30", bd=3, fg="red", bg="white")
        title.grid(column=0, row=0, columnspan=3, sticky="n", ipady=5, ipadx=100, pady=5, padx=5)
        # setting image in label
        panel = Label(self.root, image=img)
        panel.grid(column=1, row=1, columnspan=3, rowspan=2, sticky="N", padx=2, pady=2)

        # making buttons
        quitBtn = Button(self.root, text="Quit", command=lambda: self.root.destroy(), bg="white", fg="black", bd=2, activebackground="#0080ff", activeforeground="white", height=1, width=15, font="Britannic 18 bold")
        drawBtn = Button(self.root, text="Draw", command=self.directToDraw, bg="white", fg="black", bd=2, activebackground="#0080ff", activeforeground="white", height=1, width=12, font="Britannic 18 bold")
        showBtn = Button(self.root, text="Show", command=self.directToShow, bg="white", fg="black", bd=2, activebackground="#0080ff", activeforeground="white", height=1, width=12, font="Britannic 18 bold")
        speakerBtn = Button(self.root, image=speakerImg, borderwidth=0, bg="white", fg="black", bd=2, activebackground="#0080ff", activeforeground="white", height=1, width=12, font="Britannic 18 bold")

        quitBtn.grid(column=1, row=2, ipadx=7, ipady=5, sticky="S", pady=10, padx=5)
        drawBtn.grid(column=2, row=2, ipadx=7, ipady=5, sticky="S", pady=10, padx=5)
        showBtn.grid(column=3, row=2, ipadx=7, ipady=5, sticky="S", pady=10, padx=5)
        #speakerBtn.grid(column=3, row=1, sticky="NE", padx=10, pady=10)

        self.root.mainloop()

    def directToDraw(self):
        self.root.destroy()
        drawingWindow.main()

    def directToShow(self):
        self.root.destroy()
        showDrawingWindow.main()


def main():
    home()
