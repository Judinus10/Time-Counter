from tkinter import *  # Importing the tkinter module for GUI development
from playsound import playsound  # Importing playsound to play audio
import time  # Importing time module for timer functionality

# Create the main application window
root = Tk()
root.title("Timer")  # Set the title of the window
root.geometry("400x600")  # Set the size of the window
root.config(bg="#000")  # Set the background color to black
root.resizable(False, False)  # Disable resizing of the window

# Heading label
heading = Label(root, text="Timer", font="arial 30 bold", bg="#000", fg="#ea3548")
heading.pack(pady=10)

# Display current time
Label(root, font=("arial", 15, "bold"), text="current time : ", bg="papaya whip").place(x=65, y=70)

# Function to update and display the current time
def clock():
    clockTime = time.strftime('%H:%M:%S %p')  # Get the current time
    currentTime.config(text=clockTime)  # Update the label with the current time
    currentTime.after(1000, clock)  # Call the function every second

currentTime = Label(root, font=("arial", 15, "bold"), text="", bg="#fff", fg="#000")
currentTime.place(x=190, y=70)
clock()  # Start the clock

# Timer input fields for hours, minutes, and seconds
hrs = StringVar()  # Variable for hours
Entry(root, textvariable=hrs, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=30, y=155)
hrs.set("00")  # Set default value to "00"

mins = StringVar()  # Variable for minutes
Entry(root, textvariable=mins, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=150, y=155)
mins.set("00")  # Set default value to "00"

sec = StringVar()  # Variable for seconds
Entry(root, textvariable=sec, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=270, y=155)
sec.set("00")  # Set default value to "00"

# Labels for the timer fields
Label(root, text="Hours", font="arial 12", bg="#000", fg="#fff").place(x=105, y=200)
Label(root, text="Mins", font="arial 12", bg="#000", fg="#fff").place(x=225, y=200)
Label(root, text="Sec", font="arial 12", bg="#000", fg="#fff").place(x=345, y=200)

# Timer function
def timer():
    button.pack_forget()  # Remove the Start button

    # Create Pause, Resume, and Stop buttons
    pauseButton = Button(root, text="Pause", bg="#ea3548", bd=0, fg="#fff", width=10, height=2, font="arial 10 bold", command=pauseTimer)
    pauseButton.place(x=50, y=500)
    resumeButton = Button(root, text="Resume", bg="#ea3548", bd=0, fg="#fff", width=10, height=2, font="arial 10 bold", command=resumeTimer)
    resumeButton.place(x=150, y=500)
    stopButton = Button(root, text="Stop", bg="#ea3548", bd=0, fg="#fff", width=10, height=2, font="arial 10 bold", command=stopTimer)
    stopButton.place(x=250, y=500)

    global running, paused, remaining_time
    running = True  # Flag to keep the timer running
    paused = False  # Flag to check if the timer is paused

    # Calculate the total time in seconds
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())

    # Timer loop
    while times > -1 and running:
        if paused:  # If the timer is paused, wait and update the GUI
            root.update()
            time.sleep(1)
            continue

        # Calculate hours, minutes, and seconds
        minute, second = (times // 60, times % 60)
        hours = 00
        if minute > 60:
            hours, minute = (minute // 60, minute % 60)

        # Update the timer fields
        sec.set(second)
        mins.set(minute)
        hrs.set(hours)

        root.update()  # Update the GUI
        time.sleep(1)  # Wait for 1 second

        # Play sound when the timer reaches zero
        if times == 0:
            playsound("assets/audio/open.mp3")
            sec.set("00")
            mins.set("00")
            hrs.set("00")

        times -= 1  # Decrement the time

# Flags to manage timer states
running = False
paused = False

# Pause the timer
def pauseTimer():
    global paused
    paused = True

# Resume the timer
def resumeTimer():
    global paused
    paused = False

# Stop the timer
def stopTimer():
    global running
    running = False  # Stop the timer loop
    sec.set("00")
    mins.set("00")
    hrs.set("00")

# Predefined timer settings
def brush():
    hrs.set("00")
    mins.set("02")
    sec.set("00")

def face():
    hrs.set("00")
    mins.set("15")
    sec.set("00")

def eggs():
    hrs.set("00")
    mins.set("10")
    sec.set("00")

# Start button
button = Button(root, text="Start", bg="#ea3548", bd=0, fg="#fff", width=20, height=2, font="arial 10 bold", command=timer)
button.pack(padx=5, pady=40, side=BOTTOM)

# Timer setting buttons with images
Image1 = PhotoImage(file="assets/images/brush.png")
button1 = Button(root, image=Image1, bg="#000", bd=0, command=brush)
button1.place(x=7, y=300)

Image2 = PhotoImage(file="assets/images/face.png")
button2 = Button(root, image=Image2, bg="#000", bd=0, command=face)
button2.place(x=137, y=300)

Image3 = PhotoImage(file="assets/images/eggs.png")
button3 = Button(root, image=Image3, bg="#000", bd=0, command=eggs)
button3.place(x=267, y=300)

# Stop the timer when the window is closed
def on_close():
    global running
    running = False  # Stop the timer loop
    root.destroy()  # Destroy the window

root.protocol("WM_DELETE_WINDOW", on_close)  # Handle the window close event

root.mainloop()  # Start the main event loop
