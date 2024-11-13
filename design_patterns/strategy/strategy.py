from abc import ABC, abstractmethod

"""
Strategy pattern is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.
"""


class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass
