from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("welcome")

label1 = Label(window, text="welcome to Tkinter", font=("arial", 16, "bold"), fg="blue", bg="yellow", relief="solid")
label1.place(x=10, y=250)

button1 = Button(window, text="DEMO", font=("arial", 12, "bold"), fg="white", bg="brown", relief="ridge")
button1.place(x=110, y=110)

window.mainloop()