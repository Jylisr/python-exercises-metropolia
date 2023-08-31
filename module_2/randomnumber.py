#Module 2, task 6
import random

print("Random 3-digit combination:")
combination_3_digit = [random.randint(0, 9) for _ in range(3)]
print(combination_3_digit)

print("\nRandom 4-digit combination:")
combination_4_digit = [random.randint(1, 6) for _ in range(4)]
print(combination_4_digit)
