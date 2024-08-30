from tkinter import *
import random 
import time 
#--Imports
ablak = Tk()
ablak.title("Random")
ablak.geometry("220x80")



#--Window(ablak)

v3 = IntVar()
v3.set(0)

def roll():
	v0.set(int(random.randint(1, 6)))
def flip():
	v1.set(random.choice(['Head', 'Tail']))
	time.sleep(1)
	v3.set(1)
def quit():
	ablak.destroy()
		
#--definitons




b0 = Button(ablak, text="Roll", command=roll) #roll button
b0.pack(side=LEFT)

b1 = Button(ablak, text="Flip", command=flip) #coin button
b1.pack(side=RIGHT)

b2 = Button(ablak, text="Quit", command=quit) #exit the program button 
b2.pack()
#--Buttons

v0 = IntVar()
lab0 = Label(ablak, textvariable=v0)
lab0.pack(side=LEFT)  #dice
v0.set("")
#--
lab1 = Label(ablak, text="Dice", background="Green")
lab1.pack(side=LEFT)   #dice label
#--
v1 = StringVar()
lab2 = Label(ablak, textvariable=v1)
lab2.pack(side=RIGHT)    #coin label 
v1.set("")
#--
lab3 = Label(ablak, text="Coin", background="Yellow")
lab3.pack(side=RIGHT)

#--Labels

#--Testing

if v3 == 1:
	v0.set(9)


ablak.mainloop()
#--End of the program


