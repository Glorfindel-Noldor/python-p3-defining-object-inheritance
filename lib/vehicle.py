
class Vehicle:

    def __init__(self, x, y):
        self.wheel_size = x
        self.wheel_number = y

    def go(self):
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        return 'filling up!'