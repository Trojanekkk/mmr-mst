from graph import Graph
from kruskal import Kruskal
from prim import Prim

if __name__ == '__main__':
    # Generate new graph
    graph1 = Graph([0, 1, 2, 3], [[0,1,10],[1,2,15],[2,3,12],[1,3,10],[1,0,11],[2,3,11]])
    print(graph1.get_adjacency_list())

    # Execute Kurskal's algorithm
    kruskal_mst = Kruskal.exec(graph1)
    for edge in kruskal_mst:
        print(edge)

    # Execute Prim's algorithm
    prim_mst = Prim.exec(graph1, 0)
    for edge in prim_mst:
        print(edge)