import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


class Queue:
    """
    A queue is a linear data structure that follows the FIFO (First In First Out) principle. The first element added to the queue is the first element to be removed. A queue can be implemented using an array or a linked list. In this implementation, a list is used.

    Operations:
    - is_empty: Check if the queue is empty.
    - enqueue: Add an item to the rear of the queue.
    - dequeue: Remove an item from the front of the queue.
    - peek: Get the item at the front of the queue without removing it.
    - size: Get the number of items in the queue.
    - display: Display the items in the queue.

    Applications:
    - CPU scheduling
    - Disk scheduling
    - Printer queue
    - Call center systems
    - Breadth-first search (BFS) algorithm


    Time Complexity:
    - is_empty: O(1)
    - enqueue: O(1)
    - dequeue: O(1)
    - peek: O(1)
    - size: O(1)
    - display: O(n)

    Space Complexity:
    - O(n)


    Attributes:
    - items: A list to store the items in the queue.
    """

    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        return not self.items

    def enqueue(self, item) -> None:
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self) -> int:
        return len(self.items)

    def display(self) -> None:
        if self.is_empty():
            print("The queue is empty.")
            return

        print("Front -> ", end="")
        for item in self.items:
            print(item, end=" -> ")
        print("Rear")


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display()  # Output: Front -> 3 -> 2 -> 1 -> Rear
    print("Peek:", queue.peek())  # Output: Peek: 1
    queue.dequeue()  # Output: Dequeued 1 from the queue.
    queue.display()  # Output: Front -> 3 -> 2 -> Rear
