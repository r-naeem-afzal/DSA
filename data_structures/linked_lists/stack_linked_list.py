import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from typing import Any

from data_structures.linked_lists.node import Node


class StackLinkedList:
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


stack = StackLinkedList()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()  # Output: Stack: Top -> 3 -> 2 -> 1
print("Peek:", stack.peek())  # Output: Peek: 3
stack.pop()  # Output: Popped 3 from the stack.
stack.display()  # Output: Stack: Top -> 2 -> 1
