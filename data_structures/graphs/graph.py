from collections import defaultdict


class Graph:
    """
    A class to represent an undirected graph using an adjacency list. An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a vertex in the graph. In this implementation, a dictionary is used to store the adjacency list. The keys of the dictionary represent the vertices, and the values represent the neighbors of the corresponding vertex.

    Attributes:
    - graph: A dictionary to store the adjacency list of the graph.

    Methods:
    - add_edge(u: int, v: int) -> None: Adds an edge between vertices u and v.
    - remove_edge(u: int, v: int) -> None: Removes the edge between vertices u and v.
    - add_vertex(v: int) -> None: Adds a new vertex to the graph.
    - remove_vertex(v: int) -> None: Removes a vertex from the graph.
    - get_neighbors(v: int) -> List[int]: Returns a list of neighbors of vertex v.
    - get_vertices() -> List[int]: Returns a list of vertices in the graph.
    - is_edge(u: int, v: int) -> bool: Returns True if there is an edge between vertices u and v, False otherwise.
    - is_vertex(v: int) -> bool: Returns True if vertex v is in the graph, False otherwise.
    - show_graph() -> None: Displays the adjacency list of the graph.

    Applications:
    - Social networks
    - Computer networks
    - Routing algorithms

    """

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u: int, v: int) -> None:
        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_edge(self, u: int, v: int) -> None:
        if self.is_edge(u, v):
            self.graph[u].remove(v)
            self.graph[v].remove(u)

    def add_vertex(self, v: int) -> None:
        if v not in self.graph:
            self.graph[v] = []

    def remove_vertex(self, v: int) -> None:
        if v in self.graph:
            del self.graph[v]
            for key in self.graph:
                if v in self.graph[key]:
                    self.graph[key].remove(v)

    def get_neighbors(self, v: int) -> list[int]:
        return self.graph[v]

    def get_vertices(self) -> list[int]:
        return list(self.graph.keys())

    def is_edge(self, u: int, v: int) -> bool:
        return v in self.graph[u]

    def is_vertex(self, v: int) -> bool:
        return v in self.graph

    def show_graph(self) -> None:
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.show_graph()
    # Output:
    # 0 -> [1, 2]
    # 1 -> [0, 2]
    # 2 -> [0, 1, 3]
    # 3 -> [2]
    print(graph.get_neighbors(2))  # Output: [0, 1, 3]
    print(graph.get_vertices())  # Output: [0, 1, 2, 3]
    print(graph.is_edge(1, 2))  # Output: True
    print(graph.is_vertex(4))  # Output: False
    graph.remove_edge(1, 2)
    graph.remove_vertex(0)
    graph.show_graph()
    # Output:
    # 1 -> []
    # 2 -> [3]
    # 3 -> [2]
