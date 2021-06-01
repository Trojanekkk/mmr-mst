class Prim:

    # Execute Prim's algorithm on provided graph starting from predefined root
    def __init__(graph, root) -> list:
        mst = []
        mst_nodes = []
        available_edges = []
        current_node = root
        adjacency_list = graph.get_adjacency_list()

        while (len(mst_nodes) < len(graph.get_graph_order())):
            if (current_node not in mst_nodes):
                mst_nodes.append(current_node)

            
