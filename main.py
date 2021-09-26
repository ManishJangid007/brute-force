from tkinter import *
from PIL import ImageTk, Image
import re
from brute_force_module import BruteForce

root = Tk()
root.geometry("880x480")
root.title("Brute Force")

root.resizable(False, False)

# Colors
purpleText = "#783f98"
lightPurple = "#e4d0e5"
creamPurple = "#d8b0d3"
purple = "#82499d"
darkText = "#434343"
yellow = "#ffc520"
white = "#ffffff"
red = "#ef4748"

# Font
font = "Bahnschrift"

# Pngs
backgroundPng = ImageTk.PhotoImage(Image.open("assets/background.png"))
entryFieldPng = ImageTk.PhotoImage(Image.open("assets/entryField.png"))
startButtonPng = ImageTk.PhotoImage(Image.open("assets/startButton.png"))
timePlatesPng = ImageTk.PhotoImage(Image.open("assets/timePlates.png"))
resetButtonPng = ImageTk.PhotoImage(Image.open("assets/resetButton.png"))

background = Label(root, bd=0, image=backgroundPng)
background.place(x=-15, y=0)

titleMsg = Label(root, bd=0, text="Enter Your Password to Check How Secure Your Password (3-6)", fg=purpleText, font=(font, 15, 'normal'), bg=lightPurple)
titleMsg.place(x=150, y=110)

entryField = Label(root, bd=0, image=entryFieldPng, bg=lightPurple)
entryField.place(x=200, y=150)

passwordEntry = Entry(root, bg=creamPurple, fg=purpleText, bd=0, width=25, font=(font, 15, 'normal'), justify="center")
passwordEntry.place(x=217, y=155)
passwordEntry.insert(0, "Your Password")

timePlates = Label(root, bd=0, image=timePlatesPng, bg=white)
timePlates.place(x=40, y=250)

hoursLabel = Label(root, bd=0, text="Hours", fg=purpleText, bg=creamPurple, font=(font, 25, 'normal'))
hoursLabel.place(x=200, y=251)
hoursEntry = Entry(root, bd=0, bg=purple, fg=white, width=8, font=(font, 18, 'normal'), justify="center")
hoursEntry.place(x=55, y=259)
hoursEntry.insert(0, "0")

minutesLabel = Label(root, bd=0, text="Minutes", fg=purpleText, bg=creamPurple, font=(font, 25, 'normal'))
minutesLabel.place(x=150, y=318)
minutesEntry = Entry(root, bd=0, bg=purple, fg=white, width=8, font=(font, 18, 'normal'), justify="center")
minutesEntry.place(x=297, y=325)
minutesEntry.insert(0, "00")

secondsLabel = Label(root, bd=0, text="Seconds", fg=purpleText, bg=creamPurple, font=(font, 25, 'normal'))
secondsLabel.place(x=185, y=385)
secondsEntry = Entry(root, bd=0, bg=purple, fg=white, width=8, font=(font, 18, 'normal'), justify="center")
secondsEntry.place(x=56, y=393)
secondsEntry.insert(0, "00")

attemptsLabel = Label(root, bd=0, text="Total Attempts", bg=yellow, fg=darkText, font=(font, 25, 'normal'))
attemptsLabel.place(x=550, y=245)
attemptsEntry = Entry(root, bd=0, bg=yellow, width=8, fg=darkText, font=(font, 35, 'normal'), justify="center")
attemptsEntry.place(x=555, y=310)
attemptsEntry.insert(0, "0000")

noteLabel = Label(root, text="*Note : - Results are on Average Basis", bd=0, bg=yellow, fg=darkText, font=(font, 8, 'normal'))
noteLabel.place(x=472, y=437)

def start_button_func():
    main_password = passwordEntry.get()
    password_length = len(main_password)
    x = re.findall("[a-zA-z]", main_password)
    if x:
        titleMsg.config(text="Please Enter 3-6 Digit Pin", fg=red)
        titleMsg.place(x=240, y=110)
        return

    if password_length == 3:
        titleMsg.config(text="You Can Check Attempts On Terminal", fg=purpleText)
        titleMsg.place(x=270, y=110)

        attempts, guessed_password, hours, minutes, seconds = BruteForce(initial_password=main_password).pin3()

        hoursEntry.delete(0, END)
        hoursEntry.insert(0, hours)

        minutesEntry.delete(0, END)
        minutesEntry.insert(0, minutes)

        secondsEntry.delete(0, END)
        secondsEntry.insert(0, seconds)

        attemptsEntry.delete(0, END)
        attemptsEntry.insert(0, attempts)
        return

    elif password_length == 4:
        titleMsg.config(text="You Can Check Attempts On Terminal", fg=purpleText)
        titleMsg.place(x=270, y=110)

        attempts, guessed_password, hours, minutes, seconds = BruteForce(initial_password=main_password).pin4()

        hoursEntry.delete(0, END)
        hoursEntry.insert(0, hours)

        minutesEntry.delete(0, END)
        minutesEntry.insert(0, minutes)

        secondsEntry.delete(0, END)
        secondsEntry.insert(0, seconds)

        attemptsEntry.delete(0, END)
        attemptsEntry.insert(0, attempts)
        return

    elif password_length == 5:
        titleMsg.config(text="You Can Check Attempts On Terminal", fg=purpleText)
        titleMsg.place(x=270, y=110)

        attempts, guessed_password, hours, minutes, seconds = BruteForce(initial_password=main_password).pin5()

        hoursEntry.delete(0, END)
        hoursEntry.insert(0, hours)

        minutesEntry.delete(0, END)
        minutesEntry.insert(0, minutes)

        secondsEntry.delete(0, END)
        secondsEntry.insert(0, seconds)

        attemptsEntry.delete(0, END)
        attemptsEntry.insert(0, attempts)
        return

    elif password_length == 6:
        titleMsg.config(text="You Can Check Attempts On Terminal", fg=purpleText)
        titleMsg.place(x=270, y=110)

        attempts, guessed_password, hours, minutes, seconds = BruteForce(initial_password=main_password).pin6()

        hoursEntry.delete(0, END)
        hoursEntry.insert(0, hours)

        minutesEntry.delete(0, END)
        minutesEntry.insert(0, minutes)

        secondsEntry.delete(0, END)
        secondsEntry.insert(0, seconds)

        attemptsEntry.delete(0, END)
        attemptsEntry.insert(0, attempts)
        return

    elif password_length == 7:
        titleMsg.config(text="Enter Your Password to Check How Secure Your Password (3-6)", fg=purpleText)
        titleMsg.place(x=150, y=110)

        attempts, guessed_password, hours, minutes, seconds = BruteForce(initial_password=main_password).pin7()

        hoursEntry.delete(0, END)
        hoursEntry.insert(0, hours)

        minutesEntry.delete(0, END)
        minutesEntry.insert(0, minutes)

        secondsEntry.delete(0, END)
        secondsEntry.insert(0, seconds)

        attemptsEntry.delete(0, END)
        attemptsEntry.insert(0, attempts)
        return

    elif password_length == 8:
        titleMsg.config(text="Enter Your Password to Check How Secure Your Password (3-6)", fg=purpleText)
        titleMsg.place(x=150, y=110)

        attempts, guessed_password, hours, minutes, seconds = BruteForce(initial_password=main_password).pin8()

        hoursEntry.delete(0, END)
        hoursEntry.insert(0, hours)

        minutesEntry.delete(0, END)
        minutesEntry.insert(0, minutes)

        secondsEntry.delete(0, END)
        secondsEntry.insert(0, seconds)

        attemptsEntry.delete(0, END)
        attemptsEntry.insert(0, attempts)
        return

    else:
        titleMsg.config(text="Please Enter 3-6 Digit Pin", fg=red)
        titleMsg.place(x=240, y=110)
        return

startButton = Button(root, image=startButtonPng, bg=lightPurple, activebackground=lightPurple, bd=0, command=start_button_func)
startButton.place(x=520, y=150)

def reset_button_func():
    titleMsg.config(text="Enter Your Password to Check How Secure Your Password (3-6)", fg=purpleText)
    titleMsg.place(x=150, y=110)

    attemptsEntry.delete(0, END)
    attemptsEntry.insert(0, "0000")

    passwordEntry.delete(0, END)
    passwordEntry.insert(0, "Your Password")

    hoursEntry.delete(0, END)
    hoursEntry.insert(0, "0")

    minutesEntry.delete(0, END)
    minutesEntry.insert(0, "00")

    secondsEntry.delete(0, END)
    secondsEntry.insert(0, "00")

resetButton = Button(root, image=resetButtonPng, bg=yellow, bd=0, activebackground=yellow, command=reset_button_func)
resetButton.place(x=725, y=418)

root.mainloop()
