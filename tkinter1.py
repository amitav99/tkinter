from tkinter import *

# create a root window or a basic gui.
root = Tk()

# creates a frame inside the root window
frame = Frame(root)

# geometry method
frame.pack()

#button inside frame
#the frame is inside the root
button=Button(frame, text = 'ok')
button.pack()

# tkinter event in loop
root.mainloop()
