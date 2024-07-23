import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from typing import Any


class Stack:
    def __init__(self) -> None:
        self.stack = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def push(self, item: Any) -> None:
        self.stack.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            print("Stack is empty.")
            return
        return self.stack.pop()

    def peek(self) -> Any:
        """
        Return the top element of the stack.
        """

        if not self.is_empty():
            return self.stack[-1]
        print("Stack is empty.")

    def display(self) -> None:
        if self.is_empty():
            print("Stack is empty.")
            return

        print("Stack:", " -> ".join(str(item) for item in self.stack))


# ---------------------------------- EXAMPLE --------------------------------- #
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()  # Output: Stack: [1, 2, 3]
print("Peek:", stack.peek())  # Output: Peek: 3
stack.pop()  # Output: Popped 3 from the stack.
stack.display()  # Output: Stack: [1, 2]
