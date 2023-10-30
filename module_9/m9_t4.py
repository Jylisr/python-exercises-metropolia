#module 9, task 3
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

    def drive(self, hours):
        self.tra_dis += hours * self.cur_spd
        print(self.tra_dis)
        return(self.tra_dis)

def print_table(cars):
    print("{:<10} {:<15} {:<15} {:<15}".format("Reg Num", "Max Speed (km/h)", "Current Speed (km/h)", "Distance (km)"))
    for car in cars:
        print("{:<10} {:<15} {:<15} {:<15}".format(car.reg_num, car.max_spd, car.cur_spd, car.tra_dis))

def main():
    cars = []
    for i in range(1, 11):
        reg_num = "ABC-" + str(i)
        max_spd = random.randint(100, 200)
        cars.append(Car(reg_num, max_spd))

    race_distance = 10000
    hour = 1

    while all(car.tra_dis < race_distance for car in cars):
        print(f"\nHour {hour} of the race:")
        for car in cars:
            car.accelerate()
            car.drive()
        print_table(cars)
        hour += 1

    print("\nRace Results:")
    print_table(cars)

if __name__ == "__main__":
    main()
