import random
from datetime import datetime


class BruteForce():
    def __init__(self, initial_password):
        self.initial_password = initial_password
        self.spent_hours = 0
        self.spent_minutes = 0
        self.spent_seconds = 0

    def pin3(self):
        start_time = datetime.now()
        attempt = 0
        while True:
            attempt += 1
            generated_password = random.randrange(0, 1000)
            if generated_password <= 9:
                guessed_password = "00" + str(generated_password)
            elif generated_password <= 99:
                guessed_password = "0" + str(generated_password)
            else:
                guessed_password = str(generated_password)
            print("\t" + guessed_password)
            if guessed_password == self.initial_password:
                end_time = datetime.now()
                difference = str(end_time - start_time)
                extracted_time = difference.split(":")
                print(extracted_time)
                self.spent_hours = extracted_time[0]
                self.spent_minutes = extracted_time[1]
                self.spent_seconds = extracted_time[2]

                print("Your Password is : " + str(guessed_password))
                print("Attempts : " + str(attempt))
                break
        return attempt, guessed_password, self.spent_hours, self.spent_minutes, self.spent_seconds

    def pin4(self):
        start_time = datetime.now()
        attempt = 0
        while True:
            attempt += 1
            generated_password = random.randrange(0, 10000)
            if generated_password <= 9:
                guessed_password = "000" + str(generated_password)
            elif generated_password <= 99:
                guessed_password = "00" + str(generated_password)
            elif generated_password <= 999:
                guessed_password = "0" + str(generated_password)
            else:
                guessed_password = str(generated_password)
            print("\t" + guessed_password)
            if guessed_password == self.initial_password:
                end_time = datetime.now()
                difference = str(end_time - start_time)
                extracted_time = difference.split(":")
                self.spent_hours = extracted_time[0]
                self.spent_minutes = extracted_time[1]
                self.spent_seconds = extracted_time[2]

                print("Your Password is : " + str(guessed_password))
                print("Attempts : " + str(attempt))
                break
        return attempt, guessed_password, self.spent_hours, self.spent_minutes, self.spent_seconds

    def pin5(self):
        start_time = datetime.now()
        attempt = 0
        while True:
            attempt += 1
            generated_password = random.randrange(0, 100000)
            if generated_password <= 9:
                guessed_password = "0000" + str(generated_password)
            elif generated_password <= 99:
                guessed_password = "000" + str(generated_password)
            elif generated_password <= 999:
                guessed_password = "00" + str(generated_password)
            elif generated_password <= 9999:
                guessed_password = "0" + str(generated_password)
            else:
                guessed_password = str(generated_password)
            print("\t" + guessed_password)
            if guessed_password == self.initial_password:
                end_time = datetime.now()
                difference = str(end_time - start_time)
                extracted_time = difference.split(":")
                self.spent_hours = extracted_time[0]
                self.spent_minutes = extracted_time[1]
                self.spent_seconds = extracted_time[2]

                print("Your Password is : " + str(guessed_password))
                print("Attempts : " + str(attempt))
                break
        return attempt, guessed_password, self.spent_hours, self.spent_minutes, self.spent_seconds

    def pin6(self):
        start_time = datetime.now()
        attempt = 0
        while True:
            attempt += 1
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
            print("\t" + guessed_password)
            if guessed_password == self.initial_password:
                end_time = datetime.now()
                difference = str(end_time - start_time)
                extracted_time = difference.split(":")
                self.spent_hours = extracted_time[0]
                self.spent_minutes = extracted_time[1]
                self.spent_seconds = extracted_time[2]

                print("Your Password is : " + str(guessed_password))
                print("Attempts : " + str(attempt))
                break
        return attempt, guessed_password, self.spent_hours, self.spent_minutes, self.spent_seconds

    def pin7(self):
        start_time = datetime.now()
        attempt = 0
        while True:
            attempt += 1
            generated_password = random.randrange(0, 10000000)
            if generated_password <= 9:
                guessed_password = "000000" + str(generated_password)
            elif generated_password <= 99:
                guessed_password = "00000" + str(generated_password)
            elif generated_password <= 999:
                guessed_password = "0000" + str(generated_password)
            elif generated_password <= 9999:
                guessed_password = "000" + str(generated_password)
            elif generated_password <= 99999:
                guessed_password = "00" + str(generated_password)
            elif generated_password <= 999999:
                guessed_password = "0" + str(generated_password)
            else:
                guessed_password = str(generated_password)
            # print("\t" + guessed_password)
            if guessed_password == self.initial_password:
                end_time = datetime.now()
                difference = str(end_time - start_time)
                extracted_time = difference.split(":")
                self.spent_hours = extracted_time[0]
                self.spent_minutes = extracted_time[1]
                self.spent_seconds = extracted_time[2]

                print("Your Password is : " + str(guessed_password))
                print("Attempts : " + str(attempt))
                break
        return attempt, guessed_password, self.spent_hours, self.spent_minutes, self.spent_seconds

    def pin8(self):
        start_time = datetime.now()
        attempt = 0
        while True:
            attempt += 1
            generated_password = random.randrange(0, 100000000)
            if generated_password <= 9:
                guessed_password = "0000000" + str(generated_password)
            elif generated_password <= 99:
                guessed_password = "000000" + str(generated_password)
            elif generated_password <= 999:
                guessed_password = "00000" + str(generated_password)
            elif generated_password <= 9999:
                guessed_password = "0000" + str(generated_password)
            elif generated_password <= 99999:
                guessed_password = "000" + str(generated_password)
            elif generated_password <= 999999:
                guessed_password = "00" + str(generated_password)
            elif generated_password <= 9999999:
                guessed_password = "0" + str(generated_password)
            else:
                guessed_password = str(generated_password)
            # print("\t" + guessed_password)
            if guessed_password == self.initial_password:
                end_time = datetime.now()
                difference = str(end_time - start_time)
                extracted_time = difference.split(":")
                self.spent_hours = extracted_time[0]
                self.spent_minutes = extracted_time[1]
                self.spent_seconds = extracted_time[2]

                print("Your Password is : " + str(guessed_password))
                print("Attempts : " + str(attempt))
                break
        return attempt, guessed_password, self.spent_hours, self.spent_minutes, self.spent_seconds

    def alpha(self, length=6):
        start_time = datetime.now()

        small_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeric = "0123456789"
        symbols = "@\/%&*_"
        alpha_numeric_symbolic = str(small_case) + str(upper_case) + str(numeric) + str(symbols)
        attempt = 0

        while True:
            attempt += 1
            guessed_password = "".join(random.sample(alpha_numeric_symbolic, length))
            print("\t" + guessed_password)
            if guessed_password == self.initial_password:
                end_time = datetime.now()
                difference = str(end_time - start_time)
                extracted_time = difference.split(":")
                self.spent_hours = extracted_time[0]
                self.spent_minutes = extracted_time[1]
                self.spent_seconds = extracted_time[2]

                print("Your Password is : " + str(guessed_password))
                print("Attempts : " + str(attempt))
                break
        return attempt, guessed_password, self.spent_hours, self.spent_minutes, self.spent_seconds


if __name__ == "__main__":
    password = 450452
    BruteForce(initial_password=str(password)).pin6()
