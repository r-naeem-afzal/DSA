from node import Node
from typing import Any


class SinglyLinkedList:
    def __init__(self) -> None:
        self.first_node: Node | None = None

    def is_empty(self) -> bool:
        return self.first_node is None

    def append(self, data: Any) -> None:
        """
        Add a new node to the end of the list
        """
        new_node = Node(data)

        # * If the list is empty, set the new node as the first node
        if self.is_empty():
            self.first_node = new_node
            return

        # ?  Traverse the list to find the last node
        # Start at the first node
        current_node = self.first_node
        # Loop until the last node is found
        while current_node.next_node is not None:
            # * Move to the next node
            current_node = current_node.next_node

        # * Set the next node of the last node to the new node
        current_node.next_node = new_node

    def prepend(self, data: Any) -> None:
        """
        Add a new node to the beginning of the list
        """

        new_node = Node(data)

        # * Set the next node of the new node to the first node
        new_node.next_node = self.first_node

        # * Set the new node as the first node
        self.first_node = new_node

    def insert(self, data: Any, index: int) -> None:
        """
        Add a new node at a specific index
        """
        # * If the index is 0, use the prepend method
        if index == 0:
            self.prepend(data)
            return

        new_node = Node(data)

        # ? Traverse the list to find the node before the index
        # Start at the first node
        current_node = self.first_node
        # Loop until the node before the index is found
        for _ in range(index - 1):
            # * Move to the next node
            current_node = current_node.next_node

        # * Set the next node of the new node to the next node of the current node right)
        new_node.next_node = current_node.next_node
        # * Set the next node of the current node to the new node
        # (the new node is now between the current node and the next node of the current node)
        current_node.next_node = new_node

    def remove(self, data: Any) -> None:
        """
        Remove the first node with the specified data
        """

        # * If the list is empty, return
        if self.is_empty():
            return

        # * If the first node contains the data, set the next node as the first node
        if self.first_node.data == data:
            self.first_node = self.first_node.next_node
            return

        # ? Traverse the list to find the node before the node with the data
        # Start at the first node
        current_node = self.first_node
        # Loop until the node before the node with the data is found
        while (
            current_node.next_node is not None and current_node.next_node.data != data
        ):
            # * Move to the next node
            current_node = current_node.next_node

        # * If the node with the data is found, set the next node of the current node to the next node of the node with the data
        # if it is not the last node
        if current_node.next_node is not None:
            current_node.next_node = current_node.next_node.next_node

    def pop(self, index: int) -> None:
        """
        Remove the node at a specific index
        """
        # * If the index is 0, set the next node as the first node
        if index == 0:
            self.first_node = self.first_node.next_node
            return

        # ? Traverse the list to find the node before the index
        # Start at the first node
        current_node = self.first_node
        # Loop until the node before the index is found
        for _ in range(index - 1):
            # * Move to the next node
            current_node = current_node.next_node

        # * Set the next node of the current node to the next node of the next node of the current node
        # (the node at the index is now removed)
        current_node.next_node = current_node.next_node.next_node

    def __str__(self) -> str:
        """
        Return a string representation of the list
        """
        # * If the list is empty, return an empty string
        if self.is_empty():
            return ""

        # ? Traverse the list to create a string representation
        # Start at the first node
        current_node = self.first_node
        # Create an empty string
        string = ""
        # Loop until the last node is found
        while current_node is not None:
            # * Add the data of the current node to the string
            string += str(current_node.data)
            # * Move to the next node
            current_node = current_node.next_node
            # * If the current node is not the last node, add a separator
            if current_node is not None:
                string += " -> "

        return string


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
