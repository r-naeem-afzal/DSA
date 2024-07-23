from typing import Any

from data_structures.linked_lists.node import Node


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def append(self, data: Any) -> None:
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
            return

        current_node = self.head
        # * iterate to the last node so we can set its next to the new node
        while current_node.next != self.head:
            current_node = current_node.next

        current_node.next = new_node
        new_node.next = self.head

    def prepend(self, data: Any) -> None:
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
            return

        current_node = self.head
        # * iterate to the last node so we can set its next to the new node
        while current_node.next != self.head:
            current_node = current_node.next

        new_node.next = self.head
        self.head = new_node
        current_node.next = self.head

    def insert(self, data: Any, index: int) -> None:
        if index == 0:
            self.prepend(data)
            return

        new_node = Node(data)

        current_node = self.head
        for _ in range(index - 1):
            if current_node.next == self.head:
                raise IndexError("Index out of range")
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

    def delete_node(self, data: Any) -> None:
        if self.is_empty():
            return

        if self.head.data == data:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next

            current_node.next = self.head.next
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next != self.head:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return

            current_node = current_node.next

    def display(self) -> None:
        if self.is_empty():
            print("The list is empty")
            return

        current_node = self.head
        while True:
            print(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break


cll = CircularLinkedList()
cll.append("A")
cll.append("B")
cll.append("C")
cll.prepend("D")
print(
    "Circular Linked List:", cll.display()
)  # Output: Circular Linked List: ['D', 'A', 'B', 'C']
cll.delete_node("B")
print("After Deleting B:", cll.display())  # Output: After Deleting B: ['D', 'A', 'C']
