from vehicle import Vehicle


class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

print(Car.__base__)
print(int.__base__)
print(Car.__class__)
print(int.__class__)