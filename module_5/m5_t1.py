#Module 5, task 1
import random

def roll_die():
    return random.randint(1, 6) 

num_dice = int(input("How many dice do you want to roll? "))

total_sum = 0

for _ in range(num_dice):
    roll_result = roll_die()
    total_sum += roll_result
    print(f"Roll: {roll_result}")

print(f"Total sum: {total_sum}")
