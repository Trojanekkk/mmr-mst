from random import choice, randint
from graph import Graph

class Generator():

    def __init__ (self, order, max_edges_per_vertex):
        self.graph = None
        self.n_scenarios = 0
        self.edges_weights = []

        vertices = [v for v in range(order)]
        edges = []
        for v in vertices:
            for i in range(0, max_edges_per_vertex):
                tmp_vertices = vertices.copy()
                tmp_vertices.pop(v)
                edges.append([v, choice(tmp_vertices), 0])
                self.edges_weights.append(randint(1,100))
        self.graph = Graph(vertices, edges)

        self.n_scenarios = len(self.edges_weights)

    def generate_scenario (self) -> list:
        self.edges_weights.append(self.edges_weights.pop(0))

        for i, e in enumerate(self.graph.edges):
            e.weight = self.edges_weights[i]

        return self.graph