from node import Node
from typing import Any


class SinglyLinkedList:
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

    def prepend(self, data: Any) -> None:
        """
        Add a new node to the beginning of the list
        """

        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

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
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, data: Any) -> None:
        """
        Remove the first node with the specified data
        """

        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next is not None and current_node.next.data != data:
            current_node = current_node.next

        if current_node.next is not None:
            current_node.next = current_node.next.next

    def pop(self, index: int) -> None:
        """
        Remove the node at a specific index
        """
        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        for _ in range(index - 1):
            current_node = current_node.next

        current_node.next = current_node.next.next

    def __str__(self) -> str:
        """
        Return a string representation of the list
        """
        if self.is_empty():
            return ""

        current_node = self.head
        string = ""
        while current_node is not None:
            string += str(current_node.data)
            current_node = current_node.next
            if current_node is not None:
                string += " -> "

        return string

    def __getitem__(self, index: int) -> Any:
        """
        Return the data of the node at the specified index
        """
        current_node = self.head
        for _ in range(index):
            if current_node is None:
                raise IndexError("Index out of range")
            current_node = current_node.next

        if current_node is None:
            raise IndexError("Index out of range")

        return current_node.data

    def __eq__(self, value: Any) -> bool:
        """
        Check if the value is equal to the list
        """
        if not isinstance(value, SinglyLinkedList):
            return False

        current_node = self.head
        other_current_node = value.head

        while current_node is not None and other_current_node is not None:
            if current_node.data != other_current_node.data:
                return False

            current_node = current_node.next
            other_current_node = other_current_node.next

        return current_node is None and other_current_node is None


if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    linked_list.append("A")
    linked_list.append("B")
    linked_list.append("C")
    linked_list.prepend("Z")
    linked_list.insert("Y", 2)

    print(linked_list)  # Output: Z -> A -> Y -> B -> C

    linked_list.remove("A")

    linked_list.pop(2)

    print(linked_list)  # Output: Z -> Y -> C
