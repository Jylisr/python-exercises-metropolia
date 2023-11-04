#Module 11, task 2

import random

class Car:
    def __init__(self, reg_num, max_spd):
        self.reg_num = reg_num
        self.max_spd = max_spd
        self.cur_spd = 0
        self.tra_dis = 0

    def accelerate(self, change_speed):
        self.cur_spd += change_speed
        if self.cur_spd < 0 or self.cur_spd > self.max_spd:
            if self.cur_spd < 0:
                self.cur_spd = 0
            elif self.cur_spd > self.max_spd:
                self.cur_spd = self.max_spd
        else:
            print(self.cur_spd)
            return self.cur_spd

    def drive(self, hours, speed):
        self.tra_dis += hours * self.cur_spd
        print(self.tra_dis)
        self.km_driven = hours * speed

def print_table(cars):
    print("{:<10} {:<15} {:<15} {:<15}".format("Reg Num", "Max Speed (km/h)", "Current Speed (km/h)", "Distance (km)"))
    for car in cars:
        print("{:<10} {:<15} {:<15} {:<15}".format(car.reg_num, car.max_spd, car.cur_spd, car.tra_dis))
'''
cars = []
for i in range(1, 11):
    reg_num = "ABC-" + str(i)
    max_spd = random.randint(100, 200)
    cars.append(Car(reg_num, max_spd))

race_distance = 10000
hour = 1

while all(car.tra_dis < race_distance for car in cars):
    print(f"Hour {hour} of the race:")
    for car in cars:
        car.accelerate(random.randint( -10, 15))
        car.drive(hour)
        print_table(cars)
        hour += 1
'''
class ElectricCar(Car): 
    def __init__(self, reg_num, max_spd, bat_cap):
        super().__init__(reg_num, max_spd)
        self.bat_cap = bat_cap


class GasolineCar(Car):
    def __init__(self, reg_num, max_spd, gas_vol):
        super().__init__(reg_num, max_spd)
        self.gas_vol = gas_vol

electric_car = ElectricCar(reg_num="ABC-15", max_spd=180, bat_cap=52.5)
gasoline_car = GasolineCar(reg_num="ACD-123", max_spd=165, gas_vol=32.3)
electric_car_spd = 180
gasoline_car_spd = 165
electric_car.drive(hours=3, speed=electric_car_spd)
gasoline_car.drive(hours=3, speed=gasoline_car_spd)

print(f"Electric Car ({electric_car.reg_num}): {electric_car.km_driven} km")
print(f"Gasoline Car ({gasoline_car.reg_num}): {gasoline_car.km_driven} km")