# images in tkinter

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("1080x1056")

image= Image.open("2.jpg")
photo= ImageTk.PhotoImage(image)

photo1=Label(image=photo)
photo1.pack()


root.mainloop()
