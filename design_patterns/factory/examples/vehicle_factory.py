import os
import sys
from abc import ABC, abstractmethod

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from factory.factory import Factory


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        return "Driving a car"


class Motorcycle(Vehicle):
    def drive(self):
        return "Riding a motorcycle"


class Truck(Vehicle):
    def drive(self):
        return "Driving a truck"


class VehicleFactory(Factory):
    def create(self, vehicle_type: str) -> Vehicle:
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "motorcycle":
            return Motorcycle()
        elif vehicle_type == "truck":
            return Truck()


if __name__ == "__main__":
    vehicle_factory = VehicleFactory()
    car = vehicle_factory.create("car")
    print(car.drive())  # Output: Driving a car

    motorcycle = vehicle_factory.create("motorcycle")
    print(motorcycle.drive())  # Output: Riding a motorcycle

    truck = vehicle_factory.create("truck")
    print(truck.drive())  # Output: Driving a truck
