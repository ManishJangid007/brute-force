
from tkinter import *
from brute_force_module import BruteForce

root = Tk()
root.geometry("400x500")
root.title("Brute Force")

passwordLabel = Label(root, text="Enter Your Password (3-6)")
passwordLabel.pack(pady=20)

textField = Entry(root, width=20)
textField.pack()

attempts_text_field = Entry(root, width=20)
attempts_text_field.pack(pady=30)
attempts_text_field.insert(0, "Attempts : ")

hoursText = Entry(root, width=20)
hoursText.pack()
hoursText.insert(0, "Hours : ")

minutesText = Entry(root, width=20)
minutesText.pack()
minutesText.insert(0, "Minutes : ")

secondsText = Entry(root, width=25)
secondsText.pack()
secondsText.insert(0, "Seconds : ")

your_password = Entry(root, width=20)
your_password.pack(pady=20)
your_password.insert(0, "Password : ")


def brute_force():
    main_password = textField.get()
    if len(main_password) == 3:
        (attempt, password, hours, minutes, seconds) = BruteForce(initial_password=main_password).pin3()
        attempts_text_field.delete(0, END)
        attempts_text_field.insert(0, "Attempts : " + str(attempt))
        hoursText.delete(0, END)
        hoursText.insert(0, "Hours : " + str(hours))
        minutesText.delete(0, END)
        minutesText.insert(0, "Minutes : " + str(minutes))
        secondsText.delete(0, END)
        secondsText.insert(0, "Seconds : " + str(seconds))
        your_password.delete(0, END)
        your_password.insert(0, "Password : " + str(password))

    elif len(main_password) == 4:
        (attempt, password, hours, minutes, seconds) = BruteForce(initial_password=main_password).pin4()
        attempts_text_field.delete(0, END)
        attempts_text_field.insert(0, "Attempts : " + str(attempt))
        hoursText.delete(0, END)
        hoursText.insert(0, "Hours : " + str(hours))
        minutesText.delete(0, END)
        minutesText.insert(0, "Minutes : " + str(minutes))
        secondsText.delete(0, END)
        secondsText.insert(0, "Seconds : " + str(seconds))
        your_password.delete(0, END)
        your_password.insert(0, "Password : " + str(password))

    elif len(main_password) == 5:
        (attempt, password, hours, minutes, seconds) = BruteForce(initial_password=main_password).pin5()
        attempts_text_field.delete(0, END)
        attempts_text_field.insert(0, "Attempts : " + str(attempt))
        hoursText.delete(0, END)
        hoursText.insert(0, "Hours : " + str(hours))
        minutesText.delete(0, END)
        minutesText.insert(0, "Minutes : " + str(minutes))
        secondsText.delete(0, END)
        secondsText.insert(0, "Seconds : " + str(seconds))
        your_password.delete(0, END)
        your_password.insert(0, "Password : " + str(password))

    elif len(main_password) == 6:
        (attempt, password, hours, minutes, seconds) = BruteForce(initial_password=main_password).pin6()
        attempts_text_field.delete(0, END)
        attempts_text_field.insert(0, "Attempts : " + str(attempt))
        hoursText.delete(0, END)
        hoursText.insert(0, "Hours : " + str(hours))
        minutesText.delete(0, END)
        minutesText.insert(0, "Minutes : " + str(minutes))
        secondsText.delete(0, END)
        secondsText.insert(0, "Seconds : " + str(seconds))
        your_password.delete(0, END)
        your_password.insert(0, "Password : " + str(password))

    else:
        passwordLabel.config(text="Enter Your Password (3-6) (Wrong Input !)")


startButton = Button(root, text="Start BruteForce", width=15, height=1, command=brute_force)
startButton.pack(pady=20)


def brute_force_alpha():
    main_password = textField.get()
    while True:
        (attempt, password, hours, minutes, seconds) = BruteForce(initial_password=main_password).alpha(length=len(main_password))
        attempts_text_field.delete(0, END)
        attempts_text_field.insert(0, "Attempts : " + str(attempt))
        hoursText.delete(0, END)
        hoursText.insert(0, "Hours : " + str(hours))
        minutesText.delete(0, END)
        minutesText.insert(0, "Minutes : " + str(minutes))
        secondsText.delete(0, END)
        secondsText.insert(0, "Seconds : " + str(seconds))
        your_password.delete(0, END)
        your_password.insert(0, "Password : " + str(password))


startWithAlpha = Button(root, text="Start With Alpha", width=20, height=1, command=brute_force_alpha)
startWithAlpha.pack(pady=20)


def clear_fun():
    textField.delete(0, END)
    attempts_text_field.delete(0, END)
    attempts_text_field.insert(0, "Attempts : ")
    hoursText.delete(0, END)
    hoursText.insert(0, "Hours : ")
    minutesText.delete(0, END)
    minutesText.insert(0, "Minutes : ")
    secondsText.delete(0, END)
    secondsText.insert(0, "Seconds : ")
    your_password.delete(0, END)
    your_password.insert(0, "Password : ")


clearButton = Button(root, text="Clear", width=15, height=1, command=clear_fun)
clearButton.pack(pady=20)

root.mainloop()
