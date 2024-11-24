from tkinter import * 
from playsound import playsound
import time

root=Tk()
root.title("Timer")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False,False)
#heading
heading=Label(root,text="Timer",font="arial 30 bold",bg="#000",fg="#ea3548")
heading.pack(pady=10)
#clock
Label(root,font=("arial",15,"bold"),text="current time : ",bg="papaya whip").place(x=65,y=70)

def clock():
    clockTime=time.strftime('%H:%M:%S %p')
    currentTime.config(text=clockTime)
    currentTime.after(1000,clock)

currentTime=Label(root,font=("arial",15,"bold"),text="",bg="#fff",fg="#000")
currentTime.place(x=190,y=70)
clock()

root.mainloop()

