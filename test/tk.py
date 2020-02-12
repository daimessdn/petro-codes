from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x600")
root.title("welcome")

img = Image.open("test.jpg")
photo = ImageTk.PhotoImage(img)

lab = Label(image=photo)
lab.pack()

def demo1():
	print("demo tkinter")

def demo2():
	exit()

label1 = Label(root, text="welcome to Tkinter")
label1.pack()

button1 = Button(root, text="demo", command=demo1)		# GROOVE, RIDGE, SUNKEN, RAISED, FLAT, SOLID
button1.pack()

button2 = Button(root, text="exit", command=demo2)		# GROOVE, RIDGE, SUNKEN, RAISED, FLAT, SOLID
button2.pack()


root.mainloop()