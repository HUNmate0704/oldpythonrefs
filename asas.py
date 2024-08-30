from tkinter import *

ablak = Tk()
ablak.geometry("300x300")
ablak.resizable(0, 0)




def kilepes():
	ablak.destroy()

Button = Button(ablak, text = "quit", bg = "Green", fg = "Blue",  command = kilepes)
Button.pack()


ablak.mainloop()
