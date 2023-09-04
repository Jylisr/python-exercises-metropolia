#Module 3, task 2
cabin = (str(input("Enter the cabin class: ")))
if cabin == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif cabin == "A":
    print("A: above the car deck, equipped with a window.")
elif cabin == "B":
    print("B: windowless cabin above the car deck.")
elif cabin == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")