import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from typing import Any
from data_structures.linked_lists.node import Node


class DoublyCircularLinkedList:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def __is_next_node_head(self, current_node: Node) -> bool:
        return current_node.next == self.head

    def __get_next_node(self, current_node: Node) -> Node:
        return current_node.next

    def append(self, data: Any) -> None:
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
            return

        current_node = self.head
        while not self.__is_next_node_head(current_node):
            current_node = self.__get_next_node(current_node)

        current_node.next = new_node
        new_node.prev = current_node
        new_node.next = self.head
        self.head.prev = new_node

    def prepend(self, data: Any) -> None:
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
            return

        current_node = self.head
        while not self.__is_next_node_head(current_node):
            current_node = self.__get_next_node(current_node)

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        current_node.next = self.head
        self.head.prev = current_node

    def insert_after(self, prev_data: Any, data: Any) -> None:
        if self.is_empty():
            return

        current_node = self.head
        while not self.__is_next_node_head(current_node):
            if current_node.data == prev_data:
                break
            current_node = self.__get_next_node(current_node)

        if current_node.data != prev_data:
            return

        new_node = Node(data)
        new_node.next = current_node.next
        new_node.prev = current_node
        current_node.next.prev = new_node
        current_node.next = new_node

    def delete_node(self, data: Any) -> None:
        if self.is_empty():
            return

        current_node = self.head
        prev_node = None
        while not self.__is_next_node_head(current_node):
            if current_node.data == data:
                break
            prev_node = current_node
            current_node = self.__get_next_node(current_node)

        if current_node.data != data:
            return

        if prev_node:
            prev_node.next = current_node.next
            current_node.next.prev = prev_node
        else:
            prev_node = self.head
            while not self.__is_next_node_head(prev_node):
                prev_node = self.__get_next_node(prev_node)
            prev_node.next = current_node.next
            current_node.next.prev = prev_node
            self.head = current_node.next

    def display(self) -> list:
        if self.is_empty():
            return []

        nodes = []
        current_node = self.head
        while not self.__is_next_node_head(current_node):
            nodes.append(current_node.data)
            current_node = self.__get_next_node(current_node)

        nodes.append(current_node.data)
        return nodes

    def display_reverse(self) -> list:
        if self.is_empty():
            return []

        nodes = []
        current_node = self.head
        while not self.__is_next_node_head(current_node):
            current_node = self.__get_next_node(current_node)

        while not self.__is_next_node_head(current_node):
            nodes.append(current_node.data)
            current_node = current_node.prev

        nodes.append(current_node.data)
        return nodes


dll = DoublyCircularLinkedList()
dll.append("A")
dll.append("B")
dll.append("C")
dll.prepend("D")
print("Forward:", dll.display())  # Output: Forward: ['D', 'A', 'B', 'C']
print("Backward:", dll.display_reverse())  # Output: Backward: ['C', 'B', 'A', 'D']
dll.insert_after("B", "E")
print(
    "After Inserting E after B:", dll.display()
)  # Output: After Inserting E after B: ['D', 'A', 'B', 'E', 'C']
dll.delete_node("A")
print(
    "After Deleting A:", dll.display()
)  # Output: After Deleting A: ['D', 'B', 'E', 'C']