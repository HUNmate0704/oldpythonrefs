from tkinter import *




felugro1 = Tk()
C =	Canvas(felugro1, height = 250, width = 300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start = 0, extent = 150, fill = "green")
line = C.create_line(10,10,130,200,fill = 'white')
C.pack()
felugro1.mainloop()
