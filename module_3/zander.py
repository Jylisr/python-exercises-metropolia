#Module 3, task 1
zander = (float(input("Enter the lenght of the zander in centimeters: ")))
short = 42 - zander
if zander >= 42:
    print("The zander fulfills the size limit")
else:
    print("Release the zander back into the lake, it has to be 42 centimeters or longer")
    print("The zander is", short, "centimeters below the limit")