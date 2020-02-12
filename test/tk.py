from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x600")
root.title("welcome")

img = Image.open("test2.jpg")
photo = ImageTk.PhotoImage(img)

lab = Label(image=photo)
lab.pack()

fn = StringVar()
ln = StringVar()
dob = StringVar()
var = StringVar()

def demo1():
	first = fn.get()
	last = ln.get()
	dobl = dob.get()
	var1 = var.get()

	print(f("your full name is {first} {last}"))
	print(f("your age is {dobl}"))
	print(f("your country is {var1}"))

def demo2():
	exit()

label0 = Label(root, text="registration form", font=("bold", 16))
label0.place(x=90, y=150)

label1 = Label(root, text="first name: ")
label1.place(x=80, y=240)
entry1 = Entry(root, textvar=fn)
entry1.place(x=240, y=242)

label2 = Label(root, text="last name: ")
label2.place(x=80, y=280)
entry2 = Entry(root, textvar=ln)
entry2.place(x=240, y=282)

label3 = Label(root, text="dob: ")
label3.place(x=80, y=320)
entry3 = Entry(root, textvar=dob)
entry3.place(x=240, y=322)

label4 = Label(root, text="country: ")
label4.place(x=80, y=360)

list1 = ["Nepal", "India", "Canada"]
droplist = OptionMenu(root, var, *list1)
var.set("select country")
droplist.config(width=15)
droplist.place(x=240, y=360)

button1 = Button(root, text="demo", command=demo1)
button1.pack()

button2 = Button(root, text="exit", command=demo2)	
button2.pack()

root.mainloop()