#Module 9, task 3

class Car:
    def __init__(self, reg_num, max_spd):
        self.reg_num = reg_num
        self.max_spd = max_spd
        self.cur_spd = 60
        self.tra_dis = 2000

    def accelerate(self):
        if self.cur_spd == 0 and self.cur_spd <= self.max_spd:
            self.cur_spd += 30
            print(self.cur_spd)
            self.cur_spd += 70
            print(self.cur_spd)
            self.cur_spd += 50
            print(self.cur_spd)
            self.cur_spd -= 200
            if self.cur_spd < 0:
                self.cur_spd = 0
                print(self.cur_spd)
                
                
    def drive(self, hours):
        self.tra_dis = hours * self.cur_spd + self.tra_dis
        print(self.tra_dis)

        
        
hours = int  
car1 = Car("ABC-123", 142)

print(f"Registration number: {car1.reg_num}")
print(f"Maximum speed: {car1.max_spd}")
print(f"Current speed: {car1.cur_spd}")
print(f"Distance travelled: {car1.tra_dis}")

car1.drive(1.5)