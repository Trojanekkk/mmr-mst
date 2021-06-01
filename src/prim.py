class Prim:

    # Execute Prim's algorithm on provided graph starting from predefined root
    def exec (graph, root) -> list:
        mst = []
        current_node = root
        mst_nodes = [current_node]
        available_edges = []

        while (len(mst_nodes) < graph.get_graph_order()):

            for edge in graph.edges:
                if (edge.source == current_node and edge.target not in mst_nodes):
                    available_edges.append(edge)

            available_edges.sort(key=lambda e: e.weight)

            cheapest_edge = available_edges.pop(0)

            mst.append(cheapest_edge)
            current_node = cheapest_edge.target

            mst_nodes.append(current_node)
             
        return mst
