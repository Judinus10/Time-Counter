from tkinter import * 
from playsound import playsound
import time

root=Tk()
root.title("Timer")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False,False)

heading=Label(root,text="Timer",font="arial 30 bold",bg="#000",fg="#ea3548")
heading.pack(pady=10)
root.mainloop()

