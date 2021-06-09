class Kruskal:

    def __init__ (self) -> None:
        self.mst = []

    # Execute Kruskal algorithm on provided graph
    def exec (self, graph) -> list:
        mst = []
        mst_nodes = []
        mst_sets = []
        sorted_edges = graph.sort_edges()
        for edge in sorted_edges:
            if (len(mst_nodes) == graph.get_graph_order()):
                print(graph.get_graph_order())
                break

            if (edge.source == edge.target):
                continue

            if (edge.source in mst_nodes and edge.target in mst_nodes):
                continue
            
            source_set = None
            for i, ms in enumerate(mst_sets):
                if (edge.source in ms):
                    source_set = i
                    
            target_set = None
            for i, ms in enumerate(mst_sets):
                if (edge.target in ms):
                    target_set = i
                    
            if (source_set == None and target_set == None):
                mst_sets.append([edge.source, edge.target])
                mst.append(edge)
            elif (source_set == None):
                mst_sets[target_set].append(edge.source)
                mst.append(edge)
            elif (target_set == None):
                mst_sets[source_set].append(edge.target)
                mst.append(edge)
            elif (source_set != target_set):
                mst.append(edge)
                if (source_set > target_set):
                    tmp = mst_sets.pop(source_set)
                    mst_sets[target_set] + tmp
                else:
                    tmp = mst_sets.pop(target_set)
                    mst_sets[source_set] + tmp
            
            if (len(mst) == graph.get_graph_order() - 1):
                break

        self.mst = mst

        return sum(e.weight for e in mst)