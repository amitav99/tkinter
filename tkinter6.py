from tkinter import *

root = Tk()
root.geometry("533x434")

def entry():
    print ("you are welcome")
frame = Frame(root, bg="grey", relief=SUNKEN, borderwidth=5)
frame.pack(side=LEFT, anchor="nw")
button = Button(frame, text="skip")
button.pack(side=LEFT, padx=20)
button2 = Button(frame, text="ok", command=entry)
button2.pack(side=LEFT, padx=20)
button3 = Button(frame, text="close", command=root.destroy)
button3.pack(side=LEFT, padx=20)

root.mainloop()
