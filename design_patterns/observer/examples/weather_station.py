import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from observer.observer import Publisher, Subscriber


# ------------------------------------- - ------------------------------------ #


class Person(Subscriber):
    def __init__(self, name: str):
        self.name = name

    def receive_notification(self, message):
        print(f"{self.name} received a notification: {message}")


# ------------------------------------- - ------------------------------------ #


class WeatherStation(Publisher):
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.receive_notification("Weather is sunny today")


if __name__ == "__main__":
    person1 = Person("Alice")
    person2 = Person("Bob")

    weather_station = WeatherStation()
    weather_station.add_subscriber(person1)
    weather_station.add_subscriber(person2)

    weather_station.notify_subscribers()
    # Output:
    # Alice received a notification: Weather is sunny today
    # Bob received a notification: Weather is sunny today

    weather_station.remove_subscriber(person2)
    weather_station.notify_subscribers()
    # Output:
    # Alice received a notification: Weather is sunny today
