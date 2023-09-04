#Module 4, task 3

smallest = None
largest = None

while True:
    num_str = input("Enter a number (or press Enter to quit): ")

    if num_str == "":
        break 

    try:
        num = float(num_str)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if smallest is None or num < smallest:
        smallest = num
    if largest is None or num > largest:
        largest = num

if smallest is not None and largest is not None:
    print(f"The smallest number entered was: {smallest}")
    print(f"The largest number entered was: {largest}")
else:
    print("No valid numbers were entered.")
