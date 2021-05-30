# Graph symbolic structure 
# G = {V, E}
# V = {v1, v2, ... vn}
# E = {(u, v, w): u, v ∈ V, w ∈ C}

# Define edge structure
class Edge:

    # Initialize new edge
    def __init__(self, source, target, weight) -> None:
        self.source = source
        self.target = target
        self.weight = weight

    # Validate source, target and weight
    @property
    def source (self) -> int:
        return self._source

    @source.setter
    def source (self, val) -> None:
        if (type(val) != int):
            raise TypeError("Wrong value of edge's source, should be an int")

        self._source = val

    @property
    def target (self) -> int:
        return self._target

    @target.setter
    def target (self, val) -> None:
        if (type(val) != int):
            raise TypeError("Wrong value of edge's target, should be an int")

        self._target = val

    @property
    def weight (self) -> int:
        return self._weight

    @weight.setter
    def weight (self, val) -> None:
        if (type(val) != int):
            raise TypeError("Wrong value of edge's weight, only ints are supported")

        self._weight = val

    def __str__ (self):
        return f'{self.source} <-{self.weight}-> {self.target}'


# Define graph structure
class Graph:

    # Initialize new graph
    def __init__ (self, vertices, edges) -> None:
        self.vertices = vertices
        self.edges = [Edge(e[0], e[1], e[2]) for e in edges]

    # Validate vertices
    @property
    def vertices (self) -> list:
        return self._vertices

    @vertices.setter
    def vertices (self, val) -> None:
        if (type(val) != list):
            raise TypeError("Inappropriate type of vertices, should be an array")

        if (len(val) < 1):
            raise TypeError("The array of vertices cannot be empty")

        self._vertices = val

    # Validate edges
    @property
    def edges (self) -> list:
        return self._edges

    @edges.setter
    def edges (self, val) -> None:
        if (type(val) != list):
            raise TypeError("Inappropriate type of edges, should be an array")

        self._edges = val

    # Calculate graph order (number of vertices)
    def get_graph_order (self) -> int:
        return len(self.vertices)

    # Calculate graph size (number of edges)
    def get_graph_size (self) -> int:
        return len(self.edges)

    # Calculate node degree
    def get_vertex_degree(self, node_index) -> int:
        pass

    # Generate adjency list
    def get_adjacency_list (self) -> list:
        adjacency_list = [[] for _ in range(self.get_graph_order())]
        for edge in self.edges:
            adjacency_list[edge.source].append(edge.target)

            if (edge.source != edge.target):
                adjacency_list[edge.target].append(edge.source)
        
        return adjacency_list

    def sort_edges (self) -> list:
        self.edges.sort(key=lambda e: e.weight)
        return self.edges

