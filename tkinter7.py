# gridlines
from tkinter import *

def getvals():
    print (f"The useername is {uservalue.get()}")
    print (f"The password is {passvalue.get()}")

root = Tk()
root.geometry("655x434")

# frame = Frame(root, borderwidth=5, bg='black', relief= SUNKEN)
# frame.pack()
user = Label(root, text="username")
user.grid()

password = Label(root, text="password")
password.grid(row=1)
#variable class in tkinter
#BooleanVar, DoubleVar, IntVar, StringVar

uservalue= StringVar()
passvalue=StringVar()

userentry= Entry(root, textvariable= uservalue)
passentry= Entry(root, textvariable= passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit", command=getvals).grid()

root.mainloop()
