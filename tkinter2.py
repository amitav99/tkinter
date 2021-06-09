# widgets and attributes label, max, minsize
from tkinter import *

root = Tk()

root.geometry("733x434")
root.minsize(250, 300)

msg = Label(text="HI WELCOME TO PYGAME") 
msg.pack()

button = Button(root, text="close", command=root.destroy)
button.pack()
root.mainloop()
