class Kruskal:

    # Execute Kruskal algorithm on provided graph
    def exec (graph) -> list:
        mst = []
        mst_nodes = []
        sorted_edges = graph.sort_edges()
        for edge in sorted_edges:
            if (len(mst_nodes) == graph.get_graph_order()):
                break

            if (edge.source == edge.target):
                continue

            if (edge.target in mst_nodes and edge.source in mst_nodes):
                continue
            else:
                mst.append(edge)
                if (edge.source not in mst_nodes):
                    mst_nodes.append(edge.source)

                if (edge.target not in mst_nodes):
                    mst_nodes.append(edge.target)

        return mst