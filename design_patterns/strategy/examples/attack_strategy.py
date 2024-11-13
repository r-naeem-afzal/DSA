import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from strategy.strategy import Strategy

# ------------------------------------- x ------------------------------------ #


class SwordAttack(Strategy):
    def execute(self):
        print("Attacking with a sword")


class BowAndArrowAttack(Strategy):
    def execute(self):
        print("Attacking with a bow and arrow")


class MagicAttack(Strategy):
    def execute(self):
        print("Attacking with magic")


# ------------------------------------- x ------------------------------------ #


class Character:
    def __init__(self, attack_strategy: Strategy):
        self._attack_strategy = attack_strategy

    def set_attack_strategy(self, attack_strategy: Strategy):
        self._attack_strategy = attack_strategy

    @property
    def attack_strategy(self):
        return self._attack_strategy

    @attack_strategy.setter
    def attack_strategy(self, attack_strategy):
        self._attack_strategy = attack_strategy

    def attack(self):
        self.attack_strategy.execute()


if __name__ == "__main__":
    character = Character(SwordAttack())
    character.attack()  # Output: Attacking with a sword

    character.attack_strategy = BowAndArrowAttack()
    character.attack()  # Output: Attacking with a bow and arrow

    character.set_attack_strategy(MagicAttack())
    character.attack()  # Output: Attacking with magic
