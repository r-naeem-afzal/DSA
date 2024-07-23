from node import Node
from typing import Any


index_error_message = "Index out of range"


class DoublyLinkedList:
    """
    A doubly linked list is a list that consists of a sequence of elements in which every element has a link to its previous element and next element.

    Operations:
    - is_empty: Check if the list is empty.
    - append: Add a new node to the end of the list.
    - prepend: Add a new node to the beginning of the list.
    - insert: Add a new node at a specific index.
    - remove: Remove a node at a specific index.

    Applications:
    - Undo functionality in text editors
    - Browser history
    - Music playlist
    - Doubly linked list is used by the LRU (Least Recently Used) cache algorithm

    Time Complexity:
    - is_empty: O(1)
    - append: O(n)
    - prepend: O(1)
    - insert: O(n)
    - remove: O(n)

    Space Complexity:
    - O(n)

    Attributes:
    - head: The first node in the list
    """

    def __init__(self) -> None:
        self.head: Node | None = None

    def is_empty(self) -> bool:
        return self.head is None

    def append(self, data: Any) -> None:
        """
        Add a new node to the end of the list
        """
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node

    def prepend(self, data: Any) -> None:
        """
        Add a new node to the beginning of the list
        """
        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

        self.head.next.prev = new_node

    def insert(self, data: Any, index: int) -> None:
        """
        Add a new node at a specific index
        """
        if index == 0:
            self.prepend(data)
            return

        new_node = Node(data)

        current_node = self.head
        for _ in range(index - 1):
            if current_node is None:
                raise IndexError(index_error_message)
            current_node = current_node.next

        new_node.next = current_node.next
        new_node.prev = current_node
        current_node.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def remove(self, index: int) -> None:
        """
        Remove a node at a specific index
        """

        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return

        current_node = self.head
        for _ in range(index - 1):
            if current_node is None:
                raise IndexError(index_error_message)
            current_node = current_node.next

        if current_node.next is None:
            raise IndexError(index_error_message)

        current_node.next = current_node.next.next
        if current_node.next is not None:
            current_node.next.prev = current_node

    def __str__(self) -> str:
        """
        Return a string representation of the list
        """
        current_node = self.head
        nodes = []
        while current_node is not None:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(nodes)

    def __len__(self) -> int:
        """
        Return the length of the list
        """
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def __getitem__(self, index: int) -> Any:
        """
        Return the data of the node at a specific index
        """
        if index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise IndexError(index_error_message)
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.data


if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.prepend(0)
    linked_list.insert(2, 2)
    linked_list.remove(2)
    print(linked_list)  # Output: 0 -> 1 -> 2 -> 3
    print(len(linked_list))  # Output: 4
    print(linked_list[2])  # Output: 2
