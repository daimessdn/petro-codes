from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("welcome")

label1 = Label(window, text="welcome to Tkinter", font=("arial", 16, "bold"), fg="blue", bg="yellow", relief="solid").pack()

window.mainloop()