from abc import ABC, abstractmethod

"""
Observer pattern is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they're observing.
"""


class Subscriber(ABC):
    @abstractmethod
    def receive_notification(self, message: str):
        pass


class Publisher(ABC):
    @abstractmethod
    def add_subscriber(self, subscriber: Subscriber):
        pass

    @abstractmethod
    def remove_subscriber(self, subscriber: Subscriber):
        pass

    @abstractmethod
    def notify_subscribers(self):
        pass
