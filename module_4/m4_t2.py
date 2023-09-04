#Module 4, task 2
while True:
    inches = float(input("Enter a lenght in inches: "))
    centimeters = inches * 2.54
    print (f"{inches} inches is equal to {centimeters} centimeters")
    if inches <0:
        break
