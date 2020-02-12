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

def demo1():
	print("demo tkinter")

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

button1 = Button(root, text="demo", command=demo1)
button1.pack()

button2 = Button(root, text="exit", command=demo2)	
button2.pack()


root.mainloop()