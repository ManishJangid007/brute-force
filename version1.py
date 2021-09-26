import random
from tkinter import *

root = Tk()
root.geometry("400x500")
root.title("Brute Force")

passwordLabel = Label(root, text="Enter Your Six Digit Password")
passwordLabel.pack(pady=20)

textField = Entry(root, width=20)
textField.pack(pady=20)


def brute_force():
    main_password = textField.get()
    if len(main_password) == 6:
        while True:
            guessed_password = random.randrange(100000, 1000000)
            print(guessed_password)
            if guessed_password == int(main_password):
                print("Your Password is : " + str(guessed_password))
                break
    else:
        passwordLabel.config(text="Enter Six Digit Password (Wrong Input !)")


startButton = Button(root, text="Start BruteForce", width=15, height=1, command=brute_force)
startButton.pack(pady=20)

root.mainloop()
