import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from singleton.singleton import Singleton


class Logger(Singleton):
    def __init__(self):
        if not hasattr(self, "logs"):
            self.logs = []

    def log(self, message):
        self.logs.append(message)

    def show_logs(self):
        for log in self.logs:
            print(log)


if __name__ == "__main__":
    logger1 = Logger()
    logger1.log("Log 1")
    logger1.log("Log 2")
    logger1.show_logs()
    # Output:
    # Log 1
    # Log 2

    logger2 = Logger()
    logger2.log("Log 3")
    logger2.show_logs()
    # Output:
    # Log 1
    # Log 2
    # Log 3

    print(logger1 is logger2)  # Output: True
    print(logger1.logs is logger2.logs)  # Output: True
    print(logger1.logs == logger2.logs)  # Output: True
    print(logger1 == logger2)  # Output: True
    print(logger1.__class__.__name__)  # Output: Logger
    print(logger2.__class__.__name__)  # Output: Logger
