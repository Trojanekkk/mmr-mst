from graph import Graph
from generator import Generator
from kruskal import Kruskal
from prim import Prim
from boruvka import Boruvka

if __name__ == '__main__':
    # Generate random graphs
    gen = Generator(10, 2)

    graphs = []
    graphs.append(gen.generate_scenario())
    graphs.append(gen.generate_scenario())

    for g in graphs:
        print(g.get_adjacency_list())

        model = Kruskal()
        kruskal_value = model.exec(g)
        print(kruskal_value)
        
        model = Prim()
        prim_value = model.exec(g, 0)
        print(prim_value)

    # boruvka_mst = Boruvka.exec(graph1)