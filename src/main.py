from graph import Graph
from generator import Generator
from spanning_tree import Spanning_tree
from kruskal import Kruskal
from prim import Prim
from boruvka import Boruvka

if __name__ == '__main__':

    # Generate graph
    gen = Generator(4, 2)

    # Generate scenarios
    scenarios = []
    for scenario in gen.edges_weights:
        scenarios.append(gen.generate_scenario())

    results = []
    for i, s in enumerate(scenarios):
        # print(s.get_adjacency_list())

        st = []
        model = Spanning_tree(s)
        for tree in model.edges:
            model.generate_conditions()
            st_value = model.exec()
            st.append(st_value)

        model = Kruskal()
        kruskal_value = model.exec(s)
        
        prim_values = []
        for v in s.vertices:
            model = Prim()
            prim_values.append(model.exec(s, v))
            prim_value = sorted(prim_values)[0]


        results.append({
            'st': st,
            'mst_kruskal': kruskal_value,
            'mst_prim': prim_value
        })

    print(results)

    # boruvka_mst = Boruvka.exec(graph1)