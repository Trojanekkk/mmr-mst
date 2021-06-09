class Boruvka:

    def exec (graph) -> list:
        super_v = []
        graph.sort_edges()
        adj = graph.get_adjacency_list()
        
        for v in graph.vertices:
            is_neighbour_in_super_v = False
            for i, sv in enumerate(super_v):
                if (adj[0][v][0] in sv):
                    sv.append(v)
                    
                    is_neighbour_in_super_v = True
                    break
            if (is_neighbour_in_super_v == False):
                super_v.append([v])

            for sv in super_v:
                # [0, 1, 3]
                for v in sv:
                    # 0