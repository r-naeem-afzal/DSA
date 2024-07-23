import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from typing import Any


class Stack:
    """
    A stack is a linear data structure that follows the Last In First Out (LIFO) principle. The last element added to the stack is the first element to be removed.

    Operations:
    - is_empty: Check if the stack is empty.
    - push: Add an element to the top of the stack.
    - pop: Remove and return the element at the top of the stack.
    - peek: Get the element at the top of the stack without removing it.
    - display: Display the elements in the stack.

    Applications:
    - Function calls and recursion
    - Undo mechanisms in text editors
    - Backtracking algorithms

    Time Complexity:
    - is_empty: O(1)
    - push: O(1)
    - pop: O(1)
    - peek: O(1)
    - display: O(n)

    Space Complexity:
    - O(n)

    Attributes:
    - items: A list to store the items in the stack.

    """

    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item: Any) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            print("Stack is empty.")
            return
        return self.items.pop()

    def peek(self) -> Any:
        """
        Return the top element of the stack.
        """

        if not self.is_empty():
            return self.items[-1]
        print("Stack is empty.")

    def display(self) -> None:
        if self.is_empty():
            print("Stack is empty.")
            return

        print("Stack:", " -> ".join(str(item) for item in self.items))


# ---------------------------------- EXAMPLE --------------------------------- #
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()  # Output: Stack: [1, 2, 3]
print("Peek:", stack.peek())  # Output: Peek: 3
stack.pop()  # Output: Popped 3 from the stack.
stack.display()  # Output: Stack: [1, 2]
