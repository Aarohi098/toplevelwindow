#import necessary libraries
from tkinter import *

root = Tk()
root.geometry('400x300')
root.title("Main")

def topwin():
    #setting up top window
    top = Toplevel()
    top.geometry('180x180')
    top.title("Top Level")
    l2 = Label(top, text="This is the top level window")
    l2.pack()
    l2.mainloop()
    
l = Label(root, text="This is the root window")
btn = Button(root, text="Click here to open another window", command=topwin)

l.pack()
btn.pack()

root.mainloop