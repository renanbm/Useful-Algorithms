from tkinter import *
import GeradorCPF
import GeradorCC

root = Tk()

topFrame = Frame(root)
topFrame.pack(side = TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

Button1 = Button(topFrame, text= "Gerar CPF", fg = "black", command = GeradorCPF.GeraCPF)
Button2 = Button(bottomFrame, text = "Gerar C.C - Santander", fg = "red", command = GeradorCC.GeradorSantander)
Button3 = Button(bottomFrame, text = "Gerar C.C - Itaú", fg = "blue", command = GeradorCC.GeradorItau)

Button1.pack()
Button2.pack(side = LEFT)
Button3.pack(side = LEFT)

root.mainloop()
