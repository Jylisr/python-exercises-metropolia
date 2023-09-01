#Module 4, task 4
import random

correct_number = random.randint(1, 10)

guess = 0
while not guess == correct_number:
    guess = (int(input("Guess a number between 1-10: ")))
    if guess > correct_number:
        print("Too high!")
    elif guess < correct_number:
        print("Too low!")
    else:
        print("Correct!")
