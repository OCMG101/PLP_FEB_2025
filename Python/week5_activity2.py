class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden.")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Test polymorphism
def move_all(vehicles):
    for v in vehicles:
        print(v.move())

if __name__ == "__main__":
    my_vehicles = [Car(), Plane(), Boat()]
    move_all(my_vehicles)