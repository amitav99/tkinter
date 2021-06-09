from tkinter import *
root= Tk()
root.geometry("633x433")
f1=Frame(root, bg="black",borderwidth=5, relief= SUNKEN)
f1.pack(side=LEFT, fill= Y)

f2=Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f2.pack(side="top", fill=X)

l=Label(f1, text="Project Tkinter")
l.pack(pady=40)

l2=Label(f2, text="welcome to tkinter",fg="green")
l2.pack()
root.mainloop()