from random import choice, randint
from graph import Graph
from kruskal import Kruskal
from prim import Prim
from boruvka import Boruvka

if __name__ == '__main__':
    # Generate random graphs
    def generate_graphs (n_graphs, order, max_edges_per_vertex) -> list:
        graphs = []
        for g in range(n_graphs):
            vertices = [v for v in range(order)]
            edges = []
            for v in vertices:
                for i in range(0, max_edges_per_vertex):
                    tmp_vertices = vertices.copy()
                    tmp_vertices.pop(v)
                    edges.append([v, choice(tmp_vertices), randint(1,10)])
            graphs.append(Graph(vertices, edges))

        return graphs

    graphs = generate_graphs (1, 20, 3)

    for g in graphs:
        print(g.get_adjacency_list())

        model = Kruskal()
        kruskal_value = model.exec(g)
        print(kruskal_value)
        
        model = Prim()
        prim_value = model.exec(g, 0)
        print(prim_value)

    # boruvka_mst = Boruvka.exec(graph1)