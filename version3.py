
from tkinter import *
from brute_force_module import BruteForce

root = Tk()
root.geometry("400x500")
root.title("Brute Force")

passwordLabel = Label(root, text="Enter Your Password (3-6)")
passwordLabel.pack(pady=20)

textField = Entry(root, width=20)
textField.pack(pady=20)


def brute_force():
    main_password = textField.get()
    if len(main_password) == 3:
        BruteForce(initial_password=main_password).pin3()
    elif len(main_password) == 4:
        BruteForce(initial_password=main_password).pin4()
    elif len(main_password) == 5:
        BruteForce(initial_password=main_password).pin5()
    elif len(main_password) == 6:
        BruteForce(initial_password=main_password).pin6()
    else:
        passwordLabel.config(text="Enter Your Password (3-6) (Wrong Input !)")


startButton = Button(root, text="Start BruteForce", width=15, height=1, command=brute_force)
startButton.pack(pady=20)

root.mainloop()
