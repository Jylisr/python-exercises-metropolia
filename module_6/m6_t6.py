#Module 6, task 6
import math

def unit_price(diameter, price):
    radius = diameter / 2
    area_cm2 = math.pi * (radius ** 2)
    area_m2 = area_cm2 / 10000
    uprice = price / area_m2
    return uprice
    

dia1 = float(input("Please enter the diameter of pizza 1: "))
pri1 = float(input("Please enter the price of pizza 1: "))
dia2 = float(input("Please enter the diameter of pizza 2: "))
pri2 = float(input("Please enter the price of pizza 2: "))

uprice1 = unit_price(dia1, pri1)
uprice2 = unit_price(dia2, pri2)

if uprice1 < uprice2:
        print("The first pizza offers better value for money")
elif uprice2 < uprice1:
    print("The second pizza offers better value for money")
elif uprice1 == uprice2:
    print("Both pizzas offer the same value for money.")
