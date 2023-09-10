#Module 5, task 3
user_input = input("Enter an integer: ")

try:
    number = int(user_input)
    if number <= 1:
        print(f"{number} is not a prime number.")
    else:
        is_prime = True 

        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
