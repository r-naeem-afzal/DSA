class MinHeap:
    """
    A MinHeap is a complete binary tree where each node is smaller than its children. The root node is the smallest element in the heap. The two main operations are insert and extract_min. The time complexity of both operations is O(log n).

    Attributes:
    - heap: A list to store the elements in the heap.

    Methods:
    - get_parent_index(index: int) -> int: Returns the index of the parent node of the node at the given index.
    - get_left_child_index(index: int) -> int: Returns the index of the left child of the node at the given index.
    - get_right_child_index(index: int) -> int: Returns the index of the right child of the node at the given index.
    - has_parent(index: int) -> bool: Returns True if the node at the given index has a parent, False otherwise.
    - has_left_child(index: int) -> bool: Returns True if the node at the given index has a left child, False otherwise.
    - has_right_child(index: int) -> bool: Returns True if the node at the given index has a right child, False otherwise.
    - insert(data: int) -> None: Inserts a new element into the heap.
    - extract_min() -> int: Removes and returns the smallest element from the heap.
    - heapify_up() -> None: Moves the last element up the heap to maintain the heap property.
    - heapify_down() -> None: Moves the first element down the heap to maintain the heap property.

    Applications:
    - Priority queues
    - Dijkstra's algorithm
    - Prim's algorithm
    - Huffman coding
    - Heap
    - Merge k sorted arrays
    - Median of a stream of numbers


    Time Complexity:
    - get_parent_index: O(1)
    - get_left_child_index: O(1)
    - get_right_child_index: O(1)
    - has_parent: O(1)
    - has_left_child: O(1)
    - has_right_child: O(1)
    - insert: O(log n)
    - extract_min: O(log n)
    - heapify_up: O(log n)
    - heapify_down: O(log n)

    Space Complexity:
    - O(n)


    """

    def __init__(self) -> None:
        self.heap = []

    def peek(self) -> int | None:
        if self.heap:
            return self.heap[0]

    def get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def get_left_child_index(self, index: int) -> int:
        return 2 * index + 1

    def get_right_child_index(self, index: int) -> int:
        return 2 * index + 2

    def has_parent(self, index: int) -> bool:
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index: int) -> bool:
        return self.get_left_child_index(index) < len(self.heap)

    def has_right_child(self, index: int) -> bool:
        return self.get_right_child_index(index) < len(self.heap)

    def insert(self, data: int) -> None:
        self.heap.append(data)
        self.heapify_up()

    def extract_min(self) -> int | None:
        if not self.heap:
            return None

        min_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down()

        return min_item

    def heapify_up(self) -> None:
        index = len(self.heap) - 1

        while (
            self.has_parent(index)
            and self.heap[index] < self.heap[self.get_parent_index(index)]
        ):
            parent_index = self.get_parent_index(index)
            self.swap(index, parent_index)
            index = parent_index

    def heapify_down(self) -> None:
        index = 0

        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)

            if (
                self.has_right_child(index)
                and self.heap[self.get_right_child_index(index)]
                < self.heap[smaller_child_index]
            ):
                smaller_child_index = self.get_right_child_index(index)

            if self.heap[index] < self.heap[smaller_child_index]:
                break

            self.swap(index, smaller_child_index)

            index = smaller_child_index

    def display(self) -> None:
        print("Heap:", self.heap)

    def swap(self, index1: int, index2: int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]


if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.insert(10)
    min_heap.insert(5)
    min_heap.insert(15)
    min_heap.insert(3)
    min_heap.insert(7)
    min_heap.display()  # Output: Heap: [3, 5, 15, 10, 7]
    print("Min item:", min_heap.extract_min())  # Output: Min item: 3
    min_heap.display()  # Output: Heap: [5, 7, 15, 10]
    print("Min item:", min_heap.extract_min())  # Output: Min item: 5
    min_heap.display()  # Output: Heap: [7, 10, 15]
    print("Min item:", min_heap.extract_min())  # Output: Min item: 7
    min_heap.display()  # Output: Heap: [10, 15]
    print("Min item:", min_heap.extract_min())  # Output: Min item: 10
    min_heap.display()  # Output: Heap: [15]
    print("Min item:", min_heap.extract_min())  # Output: Min item: 15
    min_heap.display()  # Output: Heap: []
    print("Min item:", min_heap.extract_min())  # Output: Min item: None
    min_heap.display()  # Output: Heap: []
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(7)
    min_heap.display()  # Output: Heap: [3, 5, 7]
    print("Min item:", min_heap.extract_min())  # Output: Min item: 3
    min_heap.display()  # Output: Heap: [5, 7]
    print("Min item:", min_heap.extract_min())  # Output: Min item: 5
    min_heap.display()  # Output: Heap: [7]
    print("Min item:", min_heap.extract_min())  # Output: Min item: 7
    min_heap.display()  # Output: Heap: []
    print("Min item:", min_heap.extract_min())  # Output: Min item: None
    min_heap.display()  # Output: Heap: []
