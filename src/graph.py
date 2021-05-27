# Graph symbolic structure 
# G = {V, E}
# V = {v1, v2, ... vn}
# E = {(u, v, w): u, v ∈ V, w ∈ C}

# Define graph structure
class graph:

    # Initialize new graph
    def __init__ (self, vertices, edges) -> None:
        self.vertices = vertices
        self.edges = edges

    # Validate vertices
    @property
    def vertices (self):
        return self._vertices

    @vertices.setter
    def vertices (self, val) -> list:
        if (type(val) != list):
            raise TypeError("Inappropriate type of vertices, should be an array")

        if (len(val) < 1):
            raise TypeError("The array of vertices cannot be empty")

        self._vertices = val

    # Validate edges
    @property
    def edges (self):
        return self._edges

    @edges.setter
    def edges (self, val) -> list:
        if (type(val) != list):
            raise TypeError("Inappropriate type of edges, should be an array")

        if (len(val) > 0):
            for i, v in enumerate(val):
                if (type(v) != list):
                    raise TypeError("Inappropriate type of edge, should be an array")

                if (len(v) != 3):
                    raise TypeError(f"Wrong lenght of {i}-edge, should be equal 3 and contain: start node, end node, weight")

                if (type(v[0]) != int or type(v[1]) != int):
                    raise TypeError(f"Wrong value of {i}-edge's node index, should be an int")

                if (type(v[2]) != int):
                    raise TypeError(f"Wrong value of {i}-edge's weight, only ints are supported")

        self._edges = val

    # Calculate graph order
    def get_graph_order (self) -> int:
        return len(self.vertices)

    # Calculate graph size
    def get_graph_size (self) -> int:
        return len(self.edges)

    # Calculate node degree
    def get_vertex_degree(self, node_index) -> int:
        pass