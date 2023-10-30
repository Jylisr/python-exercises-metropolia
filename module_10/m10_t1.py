#Module 10, task 1

class Elevator:

    current_floor = 1
    def __init__(self, top_floor, bottom_floor): 
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        
    def floor_up(self):
        self.current_floor += 1

    
    def floor_down(self):
        self.current_floor -= 1

    def go_to_floor(self, floor):
        while self.current_floor != floor:
            if self.current_floor > floor:
                self.floor_down()
                print(f"The elevator is at floor: {self.current_floor}")
            elif self.current_floor < floor:
                self.floor_up()
            print(f"The elevator is at floor: {self.current_floor}")



    
elevator = Elevator(5, 1)
elevator.go_to_floor(4)

