#Module 7, task 3
airports = {"EFHK" : "Helsinki-Vantaa airport",}
choice = input("Would you like to add a new airport or search and existing one? Enter add or search: ")

if choice == "add":
    while True:
        break

if choice == "search":
    while True:
        icao = input("Enter icao")
        if icao in airports:
            print(airports[])

