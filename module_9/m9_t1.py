#Module 9, task 1
class Car:
    def __init__(self, reg_num, max_spd):
        self.reg_num = reg_num
        self.max_spd = max_spd
        self.cur_spd = 0
        self.tra_dis = 0
        
    
    
car1 = Car("ABC-123", "142 kmh/h")

print(car1.reg_num)
print(car1.max_spd)
print(car1.cur_spd)
print(car1.tra_dis)