#Module 6, task 2
import random

sides = int(input("Input the number of sides on your dice: "))

def roll():
    return random.randint(1, sides)

while True:
    result = roll()
    print(f"You rolled {result}")
    if result == sides:
        break