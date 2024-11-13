import os
import sys
from abc import ABC, abstractmethod
from typing import Optional

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from factory.factory import Factory

# ------------------------------------- - ------------------------------------ #


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass


# ------------------------------------- - ------------------------------------ #
class Car(Vehicle):
    def drive(self):
        return "Driving a car"


class Motorcycle(Vehicle):
    def drive(self):
        return "Riding a motorcycle"


class Truck(Vehicle):
    def drive(self):
        return "Driving a truck"


# ------------------------------------- - ------------------------------------ #
class VehicleFactory(Factory):
    def create(self, vehicle_type: str) -> Optional[Vehicle]:
        if vehicle_type == "car":
            return Car()
        if vehicle_type == "motorcycle":
            return Motorcycle()
        if vehicle_type == "truck":
            return Truck()
        else:
            print(f"Unknown vehicle type: {vehicle_type}")
            return None


if __name__ == "__main__":
    vehicle_factory = VehicleFactory()

    car = vehicle_factory.create("car")
    if car:
        print(car.drive())  # Output: Driving a car

    motorcycle = vehicle_factory.create("motorcycle")
    if motorcycle:
        print(motorcycle.drive())  # Output: Riding a motorcycle

    truck = vehicle_factory.create("truck")
    if truck:
        print(truck.drive())  # Output: Driving a truck

    unknown = vehicle_factory.create("plane")
    if unknown:
        print(unknown.drive())  # Output: Unknown vehicle type: plane
