import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from queues.queue import Queue


class TicketingSystem:
    def __init__(self) -> None:
        self.customers = Queue()

    def new_customer(self, customer_name: str) -> None:
        self.customers.enqueue(customer_name)
        print(f'Customer "{customer_name}" added to the queue.')

    def serve_customer(self) -> None:
        customer = self.customers.dequeue()
        if customer:
            print(f'Customer "{customer}" served.')
        else:
            print("No customers in the queue.")

    def show_customers(self) -> None:
        customers = self.customers.items
        if customers:
            print("Customers in Queue:", " -> ".join(customers))
        else:
            print("No customers in the queue.")


if __name__ == "__main__":
    ticketing_system = TicketingSystem()
    ticketing_system.new_customer("Alice")
    ticketing_system.new_customer("Bob")
    ticketing_system.new_customer("Charlie")
    ticketing_system.show_customers()  # Output: Customers in Queue: Alice -> Bob -> Charlie
    ticketing_system.serve_customer()  # Output: Customer "Alice" served.
    ticketing_system.show_customers()  # Output: Customers in Queue: Bob -> Charlie
    ticketing_system.serve_customer()  # Output: Customer "Bob" served.
    ticketing_system.serve_customer()  # Output: Customer "Charlie" served.
    ticketing_system.serve_customer()  # Output: No customers in the queue.
