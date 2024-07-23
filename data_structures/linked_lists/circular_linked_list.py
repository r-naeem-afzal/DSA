from typing import Any

from data_structures.linked_lists.node import Node


class CircularLinkedList:
    """
    A circular linked list is a linked list where all nodes are connected to form a circle. Each node has a reference to the next node in the sequence. The last node points back to the first node. The list can be traversed in both directions.

    Operations:
    - is_empty: Check if the list is empty.
    - append: Add an item to the end of the list.
    - prepend: Add an item to the beginning of the list.
    - insert: Add an item at a specific index in the list.
    - delete_node: Remove an item from the list.
    - display: Display the items in the list.

    Applications:
    - Circular buffer
    - Carousel
    - Multiplayer games

    Time Complexity:
    - is_empty: O(1)
    - append: O(n)
    - prepend: O(n)
    - insert: O(n)
    - delete_node: O(n)
    - display: O(n)

    Space Complexity:
    - O(n)

    Attributes:
    - head: The first node in the list

    """

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


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append("A")
    cll.append("B")
    cll.append("C")
    cll.prepend("D")
    print(
        "Circular Linked List:", cll.display()
    )  # Output: Circular Linked List: ['D', 'A', 'B', 'C']
    cll.delete_node("B")
    print(
        "After Deleting B:", cll.display()
    )  # Output: After Deleting B: ['D', 'A', 'C']
