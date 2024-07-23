import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


from typing import Any


class CircularQueue:
    """
    A circular queue is a data structure that uses a single, fixed-size array to store elements. It follows the FIFO (First In First Out) principle. When the rear of the queue reaches the end of the array, it wraps around to the beginning of the array. This allows the queue to use the space efficiently.

    Operations:
    - is_empty: Check if the queue is empty.
    - is_full: Check if the queue is full.
    - enqueue: Add an item to the rear of the queue.
    - dequeue: Remove an item from the front of the queue.
    - peek: Get the item at the front of the queue without removing it.
    - display: Display the items in the queue.

    Applications:
    - CPU scheduling
    - Disk scheduling
    - Printer queue
    - Call center systems
    - Breadth-first search (BFS) algorithm

    Time Complexity:
    - is_empty: O(1)
    - is_full: O(1)
    - enqueue: O(1)
    - dequeue: O(1)
    - peek: O(1)
    - display: O(n)

    Space Complexity:
    - O(n)

    Attributes:
    - size: The size of the queue
    - queue: An array to store the items in the queue
    - front: The index of the front of the queue
    """

    def __init__(self, size: int) -> None:
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item: Any) -> None:
        """
        Add an item to the rear of the queue.
        """
        if self.is_full():
            print("Queue is full.")
            return

        if self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        print("self.rear", self.rear)
        self.queue[self.rear] = item

    def dequeue(self) -> Any:
        """
        Remove an item from the front of the queue.
        """
        if self.is_empty():
            print("Queue is empty.")
            return

        item = self.queue[self.front]

        if self.front == self.rear:  # If there is only one element in the queue
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return item

    def peek(self) -> Any:
        """
        Get the item at the front of the queue without removing it.
        """
        if self.is_empty():
            print("Queue is empty.")
            return

        return self.queue[self.front]

    def display(self) -> None:
        """
        Display the items in the queue.
        """
        if self.is_empty():
            print("Queue is empty.")
            return

        if self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        """
        return self.front == -1

    def is_full(self) -> bool:
        """
        Check if the queue is full.
        """
        return (self.rear + 1) % self.size == self.front


if __name__ == "__main__":
    circular_queue = CircularQueue(5)
    circular_queue.enqueue(1)
    circular_queue.enqueue(2)
    circular_queue.enqueue(3)
    circular_queue.enqueue(4)
    circular_queue.display()  # Output: Queue: 1 2 3 4
    circular_queue.dequeue()  # Output: Dequeued 1 from the queue.
    circular_queue.enqueue(5)
    circular_queue.enqueue(6)
    circular_queue.display()  # Output: Queue: 2 3 4 5 6
