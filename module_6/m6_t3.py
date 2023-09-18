#Module 6, task 3

while True:
    gallons = float(input("Enter the amount of gasoline in U.S gallons: "))


    def converter():
        liters = gallons*3.7854
        if gallons > 0:
            print(f"{gallons} U.S gallons of gasoline is equal to {liters} liters of gasoline")


    converter()

    if gallons < 0:
        break



