#Module 5, task 2
numbers = []
while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    
    if user_input == "":
        break
    else:
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if len(numbers) >= 5:
    numbers.sort(reverse=True)
    
    print("The five greatest numbers are:")
    for i in range(5):
        print(numbers[i])
else:
    print("You entered fewer than five numbers, therefore the 5 greatest can't be listed.")
