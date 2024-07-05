from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Node | None = None
        self.prev: Node | None = None
