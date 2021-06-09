class Spanning_tree:

    def __init__ (self, graph) -> None:
        self.st = []
        self.graph = graph
        self.edges = graph.edges

    # Execute Kruskal algorithm on provided graph
    def exec (self) -> list:
        st = []
        st_nodes = []
        st_sets = []
        for edge in self.edges:
            if (len(st_nodes) == self.graph.get_graph_order()):
                break

            if (edge.source == edge.target):
                continue

            if (edge.source in st_nodes and edge.target in st_nodes):
                continue
            
            source_set = None
            for i, ms in enumerate(st_sets):
                if (edge.source in ms):
                    source_set = i
                    
            target_set = None
            for i, ms in enumerate(st_sets):
                if (edge.target in ms):
                    target_set = i
                    
            if (source_set == None and target_set == None):
                st_sets.append([edge.source, edge.target])
                st.append(edge)
            elif (source_set == None):
                st_sets[target_set].append(edge.source)
                st.append(edge)
            elif (target_set == None):
                st_sets[source_set].append(edge.target)
                st.append(edge)
            elif (source_set != target_set):
                st.append(edge)
                if (source_set > target_set):
                    tmp = st_sets.pop(source_set)
                    st_sets[target_set] + tmp
                else:
                    tmp = st_sets.pop(target_set)
                    st_sets[source_set] + tmp
            
            if (len(st) == self.graph.get_graph_order() - 1):
                break

        self.st = st

        return sum(e.weight for e in st)

    def generate_conditions (self) -> None:
        self.edges.append(self.edges.pop(0))