from typing import Union


"""
Decorator pattern is a structural pattern that allows adding new behaviors to objects dynamically by placing them inside special wrapper objects that contain these behaviors.
"""


# ------------------------------------- x ------------------------------------ #
class Decorator:
    def __init__(self, coffee: Union["Coffee", "Decorator"]):
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost()


class MilkDecorator(Decorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.5


class SugarDecorator(Decorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.2


# ------------------------------------- x ------------------------------------ #
class Coffee:
    def cost(self) -> float:
        return 2


if __name__ == "__main__":
    coffee = Coffee()
    print(f"Cost of coffee: {coffee.cost()}")  # Output: Cost of coffee: 2

    milk_coffee = MilkDecorator(coffee)
    print(
        f"Cost of milk coffee: {milk_coffee.cost()}"
    )  # Output: Cost of milk coffee: 2.5

    sugar_milk_coffee = SugarDecorator(milk_coffee)
    print(
        f"Cost of sugar milk coffee: {sugar_milk_coffee.cost()}"
    )  # Output: Cost of sugar milk coffee: 2.7
