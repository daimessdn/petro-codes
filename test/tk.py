from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("welcome")

def demo1():
	print("demo tkinter")

def demo2():
	exit()

label1 = Label(window, text="welcome to Tkinter")
label1.pack()

button1 = Button(window, text="demo", command=demo1)		# GROOVE, RIDGE, SUNKEN, RAISED, FLAT, SOLID
button1.pack()

button2 = Button(window, text="exit", command=demo2)		# GROOVE, RIDGE, SUNKEN, RAISED, FLAT, SOLID
button2.pack()


window.mainloop()