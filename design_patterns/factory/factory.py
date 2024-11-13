from abc import ABC, abstractmethod

"""
Factory pattern is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
"""


class Factory(ABC):
    @abstractmethod
    def create(self):
        pass
