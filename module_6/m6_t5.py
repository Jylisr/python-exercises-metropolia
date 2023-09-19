#Module 6, task 5

def remove_odd_numbers(numbers):
    even_numbers = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    
    return even_numbers


if __name__ == "__main__":
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_list = remove_odd_numbers(int_list)

    print("Original List:", int_list)

    print("List with Odd Numbers Removed:", even_list)