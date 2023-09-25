#Module 7, task 3
airports = {"EFHK" : "Helsinki-Vantaa airport",}
choice = input("Would you like to add a new airport or search and existing one? Enter add or search, enter quit to exit: ")

while True:
    if choice == "add":
        while True:
            icao = input("Enter icao: ")
            name = input("Enter airport name: ")
            if icao or name == "":
                break
            else:
                airports.update({icao : name})
                print(airports)

    elif choice == "search":
        while True:
            icao = input("Enter icao: ")
            if icao == "":
                print(airports)
                break
            elif icao in airports:
                print(airports[icao])
    elif choice == "quit" or "":
        break

