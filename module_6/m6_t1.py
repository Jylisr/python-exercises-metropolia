#Module 6, task 1
import random

dice = random.randint(1, 6)


def roll():
    dice = random.randint(1, 6)
    print(f"You rolled {dice}")


while True:
    roll()
    if dice == 6:
        break