# Label attributes
from tkinter import *
root = Tk()
root.geometry("744x533")
root.title("calculator")

# impoartant labels
# text=adds text
# bd=background
# fg=foreground
# font =sets the font
# padx = xpadding
# pady= ypadding
# font=("ariel",25,"bold"))
# relief=border styling - SUNKEN,RIDGE,GROOVE,RAISED

message=Label(text="""  A paragraph is a series of related sentences developing\n
 a central idea, called the topic. Try to think about paragraphs in terms of thematic\n
  unity: a paragraph is a sentence or a group of sentences that supports one central, \n
  unified idea. Paragraphs add one idea at a time to your broader argument\n
""",bg="black", fg = "white", padx=20,pady=20, font=("ariel",10,"bold"),borderwidth=5,relief= SUNKEN)
# side=top, bottom, left, right
#anchor=nw/se
#fill=X,fill=y
# message.pack(side= "bottom", anchor = "se")

message.pack(side= "left", fill=Y)


button=Button(root, text="close",command=root.destroy)
button.pack()
root.mainloop()