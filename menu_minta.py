from Tkinter import*
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.LOW)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, GPIO.LOW)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.LOW)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.LOW)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.LOW)
GPIO.setup(38, GPIO.OUT)
GPIO.output(38, GPIO.LOW)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.LOW)
GPIO.setup(37, GPIO.OUT)
GPIO.output(37, GPIO.LOW)
GPIO.setup(35, GPIO.OUT)
GPIO.output(35, GPIO.LOW)
GPIO.setup(33, GPIO.OUT)
GPIO.output(33, GPIO.LOW)
GPIO.setup(31, GPIO.OUT)
GPIO.output(31, GPIO.LOW)


def donothing():
	filewin = Toplevel (ablak)
	button = Button (filewin, text="Do nothing button")
	button.pack()
	
def ki():
	ablak.destroy
	GPIO.output(11, GPIO.LOW)
	GPIO.output(13, GPIO.LOW)
	GPIO.output(15, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(18, GPIO.LOW)
	GPIO.output(22, GPIO.LOW)
	GPIO.output(38, GPIO.LOW)
	GPIO.output(40, GPIO.LOW)
	GPIO.output(37, GPIO.LOW)
	GPIO.output(35, GPIO.LOW)
	GPIO.output(33, GPIO.LOW)
	GPIO.output(31, GPIO.LOW)
	GPIO.cleanup()
	
def allon():
	print ("LED on")
	GPIO.output(11,True)
	GPIO.output(13,True)
	GPIO.output(15,True)
	GPIO.output(16,True)
	GPIO.output(18,True)
	GPIO.output(22,True)
	GPIO.output(38,True)
	GPIO.output(40,True)
	GPIO.output(37,True)
	GPIO.output(35,True)
	GPIO.output(33,True)
	GPIO.output(31,True)
def alloff():
	print ("LED off")
	GPIO.output(11,False)
	GPIO.output(13,False)
	GPIO.output(15,False)
	GPIO.output(16,False)
	GPIO.output(18,False)
	GPIO.output(22,False)
	GPIO.output(38,False)
	GPIO.output(40,False)
	GPIO.output(37,False)
	GPIO.output(35,False)
	GPIO.output(33,False)
	GPIO.output(31,False)
	
ablak = Tk()
ablak.title("Python Menu Demo")
ablak.geometry("300x300")
menubar = Menu (ablak)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="Enty field", command = donothing)
filemenu.add_command(label="Canvas", command = donothing)
filemenu.add_command(label="Radio Button", command = donothing)
filemenu.add_command(label="Check box", command = donothing)
filemenu.add_command(label="Button", command = donothing)

filemenu.add_separator()

filemenu.add_command(label =  "Exit", command = ki)
menubar.add_cascade(label =  "Widgets", menu = filemenu)
editmenu = Menu (menubar, tearoff=0)
editmenu.add_command(label = "All On", command = allon)

# editmenu.add_separator()

editmenu.add_command(label = "All Off", command = alloff)
editmenu.add_command(label = "Running light", command =donothing)
editmenu.add_command(label = "Binary counter", command =donothing)
editmenu.add_command(label = "Menu 5", command =donothing)
editmenu.add_command(label = "Menu 6", command =donothing)

menubar.add_cascade(label = "GPIO", menu = editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "Help Index", command =donothing)
helpmenu.add_command(label = "About...", command =donothing)
menubar.add_cascade(label = "Help", menu = helpmenu)

ablak.config(menu = menubar)
ablak.mainloop()