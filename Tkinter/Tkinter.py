from tkinter import *

root = Tk()

#label1 = Label(root, text = "Name:").grid(row = 0, column = 0, sticky = E)
#label2 = Label(root, text = "Password:").grid(row = 1, column = 0, sticky = E)
#Entry1 = Entry(root).grid(row = 0, column = 1)
#Entry2 = Entry(root).grid(row = 1, column = 1)
#CheckBox1 = Checkbutton(root, text = "Keep me logged in").grid(columnspan = 2)

def leftClick(event):
    print("Left")
def rightClick(event):
    print("Right")
def centerClick(event):
    print("Center")

Button1 = Button(root, text = "Click Me!")
Button1.bind("<Button-1>", leftClick)
Button1.bind("<Button-2>", centerClick)
Button1.bind("<Button-3>", rightClick)
Button1.pack()

root.mainloop()