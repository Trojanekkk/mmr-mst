from random import choice, randint

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
        kruskal_mst = Kruskal.exec(g)
        print("Kruskal")
        for i, edge in enumerate(kruskal_mst):
            print(str(i)+". ", edge)
        prim_mst = Prim.exec(g, 0)
        print("Prim")
        for i, edge in enumerate(prim_mst):
            print(str(i)+". ", edge)

    # Generate new graph
    # graph1 = Graph([0, 1, 2, 3], [[0,1,10],[1,2,15],[2,3,12],[1,3,10],[1,0,11],[2,3,11]])
    # print(graph1.get_adjacency_list())

    # Execute Kurskal's algorithm
    # kruskal_mst = Kruskal.exec(graph1)
    # for edge in kruskal_mst:
    #     print(edge)

    # Execute Prim's algorithm
    # prim_mst = Prim.exec(graph1, 0)
    # for edge in prim_mst:
    #     print(edge)

    # boruvka_mst = Boruvka.exec(graph1)