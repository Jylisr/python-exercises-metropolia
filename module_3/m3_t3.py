#Module 3, task 3
bio_gender = (str(input("Please enter your biological gender: ")))
hemoglobin = ((float(input("Please enter your hemoglobin value: "))))

if bio_gender == "male" and 167 >= hemoglobin >= 134:
    print("Your hemoglobin value is normal")
elif bio_gender == "male" and hemoglobin < 134:
    print("Your hemoglobin value is too low")
elif bio_gender == "male" and hemoglobin > 167:
    print("Your hemoglobin value is too high")

if bio_gender == "female" and 155 >= hemoglobin >= 117:
    print("Your hemoglobin value is normal")
elif bio_gender == "female" and hemoglobin < 117:
    print("Your hemoglobin value is too low")
elif bio_gender == "female" and hemoglobin > 155:
    print("Your hemoglobin value is too high")



