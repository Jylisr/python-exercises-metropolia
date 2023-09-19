#module 6, task 4

list_int = [1, 5, 6]

def addl(list_int):
    total = 0
    for i in list_int:
        total += i
    print(total)
    return total


addl(list_int)