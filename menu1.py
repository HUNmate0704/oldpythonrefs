from tkinter import *
from tkinter import messagebox


def donothing():
	filewin = Toplevel(ablak)
	b0 = Button(filewin, text="Do nothing button")
	b0.pack()




def canvas():
	felugro1 = Toplevel(ablak)
	felugro1.geometry("300x300")
	C =	Canvas(felugro1, bg = "green", height = 250, width = 300)
	coord = 10, 50, 240, 100
	arc = C.create_arc(coord, start = 30, extent = 150, fill = "red")
	line = C.create_line(10,10,130,100,fill = 'white')
	C.pack()
	
	b1 = Button(felugro1, text='Quit', command=felugro1.destroy)
	b1.pack()
	var = StringVar()
	label = Label(felugro1, textvariable = var, relief = FLAT)
	label.pack()
	
	var.set("Here, you can see a canvas")



def spinbox():
	felugro2 = Toplevel(ablak)
	felugro2.geometry("300x300")
	w1 = Spinbox(felugro2, from_ = 0, to = 10, state="readonly")
	w1.pack()
	csacska = Button(felugro2, text='Value', command=hasdads)
	csacska.pack()
	
def hasdads():
	label1 = Label(felugro2, textvariable = var1, relief = FLAT)
	label1.pack()
	var1 = StringVar()
	var1.set(w1.get())


ablak = Tk()
ablak.title("Menu")
ablak.geometry("500x500")
menubar = Menu(ablak)
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "New", command = donothing)
filemenu.add_command(label = "Open", command = donothing)
filemenu.add_command(label = "save", command = donothing)
filemenu.add_command(label = "save as...", command = donothing)
filemenu.add_command(label = "Close", command = donothing)

filemenu.add_separator()

filemenu.add_command(label = "Exit", command = ablak.destroy)

	
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Undo", command = donothing)

editmenu.add_separator()

editmenu.add_command(label = "Cut", command = donothing)
editmenu.add_command(label =  "copy", command = donothing)
editmenu.add_command(label =  "Paste", command = donothing)
editmenu.add_command(label =  "Delete", command = donothing)
editmenu.add_command(label =  "Select All", command = donothing)


spinmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Spinbox", menu = spinmenu)
spinmenu.add_command(label = "Spinbox", command = spinbox)


canvasm = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Canvas", menu = canvasm)
canvasm.add_command(label = "Canvas", command = canvas)


ablak.config(menu = menubar)
ablak.mainloop()
