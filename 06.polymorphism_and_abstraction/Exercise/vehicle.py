from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):
    #there is no modification of the init no need to write it again it will inherit the init from the base class
    def drive(self, distance: int):
        needed_quantity = (self.fuel_consumption + 0.9) * distance
        if self.fuel_quantity >= needed_quantity:
            self.fuel_quantity -= needed_quantity

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    def drive(self, distance):
        needed_quantity = (self.fuel_consumption +1.6) * distance
        if self.fuel_quantity >= needed_quantity:
            self.fuel_quantity -= needed_quantity

    def refuel(self, fuel: int):
        self.fuel_quantity += (0.95 * fuel)


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
