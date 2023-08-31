#Module 2, task 5
talents = (float(input("Enter talents: ")))
pounds = (float(input("Enter pounds: ")))
lots = (float(input("Enter lots: ")))
total_pounds = talents * 20 + pounds
total_lots = total_pounds * 32 + lots
total_grams = total_lots * 13.3
total_kilograms = total_grams // 1000
remaining_grams = total_grams % 1000
print("The weight in modern units:", total_kilograms and remaining_grams)