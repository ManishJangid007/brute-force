
# For Six Digit Password

import random
import time
from tkinter import *

root = Tk()
root.geometry("400x500")
root.title("Brute Force")

passwordLabel = Label(root, text="Enter Your Six Digit Password")
passwordLabel.pack(pady=20)

textField = Entry(root, width=20)
textField.pack(pady=20)

guessedPasswordLabel = Label(root, text="Your Password is : ")
guessedPasswordLabel.pack(pady=20)

bruteForceTextField = Entry(root, width=20)
bruteForceTextField.pack(pady=20)
bruteForceTextField.insert(0, "Press Start to Check")

attemptsLabel = Label(root, text="Attempts : ")
attemptsLabel.pack(pady=20)

attemptsTextField = Entry(root, width=20)
attemptsTextField.pack(pady=20)
attemptsTextField.insert(0, "Press Start to Check")

def brute_force():
    main_password = textField.get()
    if len(main_password) == 6:
        attempts = 0
        while True:
            bruteForceTextField.delete(0, END)
            attemptsTextField.delete(0, END)
            attempts += 1
            generated_password = random.randrange(0, 1000000)
            if generated_password <= 9:
                guessed_password = "00000" + str(generated_password)
            elif generated_password <= 99:
                guessed_password = "0000" + str(generated_password)
            elif generated_password <= 999:
                guessed_password = "000" + str(generated_password)
            elif generated_password <= 9999:
                guessed_password = "00" + str(generated_password)
            elif generated_password <= 99999:
                guessed_password = "0" + str(generated_password)
            else:
                guessed_password = str(generated_password)
            bruteForceTextField.insert(0, guessed_password)
            attemptsTextField.insert(0, attempts)
            print(guessed_password)
            if guessed_password == main_password:
                print("Your Password is : " + str(guessed_password))
                break
            time.sleep(1)
    else:
        passwordLabel.config(text="Enter Six Digit Password (Wrong Input !)")


startButton = Button(root, text="Start BruteForce", width=15, height=1, command=brute_force)
startButton.pack(pady=20)

root.mainloop()
