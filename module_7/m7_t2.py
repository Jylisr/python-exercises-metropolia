#Module 7, task 2

set_names = set("J")

while True:
    nam_es = str(input("Enter names: "))
    if nam_es == "":
        print(set_names, sep = "\n")
        break
    if nam_es in set_names:
        print("Existing name")
    else:
        print("New name")
    set_names.add(nam_es)

