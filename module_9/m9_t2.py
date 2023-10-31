#Module 9, task 2

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




        
        
    
car1 = Car("ABC-123", 142)


car1.accelerate(30)
car1.accelerate(70)
print(car1.cur_spd)
car1.accelerate(50)
print(car1.cur_spd)
car1.accelerate(-200)
print(car1.cur_spd)
