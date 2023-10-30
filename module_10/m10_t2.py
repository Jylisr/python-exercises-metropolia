#Module 10, task 2


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

class Building:
    elevators = []
    def __init__(self, top_floor, bottom_floor, elevator_num):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.elevator_amount = elevator_num
        for n in range (0, elevator_num):
            n = Elevator(self.bottom_floor, self.top_floor)
            self.elevators.append(n)


    def run_elevator(self, index, target_floor):
        self.elevators[index].go_to_floor(target_floor)


building = Building(5, 1, 7)
elevator = Elevator(5, 1)
building.run_elevator(3, 4)

