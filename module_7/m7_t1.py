#Module 7, task 1

month = int(input("Enter the number of the month: "))

seasons = ("spring", "summer", "autumn", "winter")

if 3 <= month < 6:
    print(seasons[0])
elif 6 <= month < 9:
    print(seasons[1])
elif 9 <= month < 12:
    print(seasons[2])
elif month < 3 or month == 12:
    print(seasons[3])
