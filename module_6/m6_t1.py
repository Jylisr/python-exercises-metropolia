#Module 6, task 1
import random

def roll():
    return random.randint(1, 6)



while True:
    result = roll()
    print(f"You rolled {result}")
    if result == 6:
        break