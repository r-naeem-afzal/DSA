from abc import ABC

"""
Singleton pattern is a creational design pattern that ensures a class has only one instance and provides a global point of access to it.
"""


class Singleton(ABC):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
