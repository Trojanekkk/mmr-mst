from graph import graph
from kruskal import kruskal

if __name__ == '__main__':
    # Generate new graph
    graph1 = graph([0, 1, 2, 3], [[0,1,10],[1,2,15],[2,3,12],[1,3,10],[1,0,11],[2,3,11]])
    print(graph1.get_adjacency_list())