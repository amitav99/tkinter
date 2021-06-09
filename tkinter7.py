# gridlines
from tkinter import *

root = Tk()
root.geometry("655x434")

frame = Frame(root, borderwidth=5, bg='black', relief= SUNKEN)
frame.pack()
user = Label(root, text="username")
user.pack()
password = Label(root, text="password")
password.pack()

root.mainloop()
