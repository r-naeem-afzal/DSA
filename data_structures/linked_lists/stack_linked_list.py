import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from typing import Any

from data_structures.linked_lists.node import Node


class StackLinkedList:
    """
    A stack is a linear data structure that follows the Last In First Out (LIFO) principle. The last element added to the stack is the first element to be removed. A stack can be implemented using an array or a linked list. In this implementation, a singly linked list is used.

    Operations:
    - push: Add an element to the top of the stack.
    - pop: Remove and return the element at the top of the stack.
    - peek: Get the element at the top of the stack without removing it.
    - is_empty: Check if the stack is empty.
    - display: Display the elements in the stack.

    Applications:
    - Function calls and recursion
    - Undo mechanisms in text editors
    - Backtracking algorithms

    Time Complexity:
    - push: O(1)
    - pop: O(1)
    - peek: O(1)
    - is_empty: O(1)
    - display: O(n)

    Space Complexity:
    - O(n)

    Attributes:
    - head: The top of the stack
    """

    def __init__(self) -> None:
        self.head = None

    def push(self, data: Any) -> None:
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")

        popped = self.head.data
        self.head = self.head.next

        return popped

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Cannot peek from an empty stack")

        return self.head.data

    def is_empty(self) -> bool:
        return self.head is None

    def display(self) -> None:
        if self.is_empty():
            print("The stack is empty")
            return

        stack_str = "Top -> "
        current_node = self.head
        while current_node is not None:
            stack_str += f"{current_node.data} -> "
            current_node = current_node.next

        print(f"Stack: {stack_str[:-4]}")


if __name__ == "__main__":
    stack = StackLinkedList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()  # Output: Stack: Top -> 3 -> 2 -> 1
    print("Peek:", stack.peek())  # Output: Peek: 3
    stack.pop()  # Output: Popped 3 from the stack.
    stack.display()  # Output: Stack: Top -> 2 -> 1
