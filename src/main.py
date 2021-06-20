from graph import Graph
from generator import Generator
from spanning_tree import Spanning_tree
from kruskal import Kruskal
from prim import Prim

if __name__ == '__main__':

    # Generate graph
    gen = Generator(5, 2)

    results = []
    for i, s in enumerate(range(gen.n_scenarios)):
        s = gen.generate_scenario()
        # print(s.get_adjacency_list())

        st = []
        model = Spanning_tree(s)
        for tree in model.edges:
            model.generate_conditions()
            st_value = model.exec()
            st.append(st_value)

        model = Kruskal()
        kruskal_value = model.exec(s)
        
        # prim_values = []
        # for v in s.vertices:
        #     model = Prim()
        #     prim_values.append(model.exec(s, v))
        #     prim_value = sorted(prim_values)[0]

        results.append({
            'st': st,
            'avg': sum(st)/len(st),
            'mst_kruskal': kruskal_value,
            # 'mst_prim': prim_value
        })


    # Print found in graph STs and MST values for every scenario
    print('Matrix of scenarios and spanning tree costs:\n', results, '\n')

    # Calculate Regrets
    regrets = []
    for s in results:
        regret = {'st': []}
        mst = s['mst_kruskal']
        for st in s['st']:
            regret['st'].append(st - mst)
        regrets.append(regret)
    print('Matrix of regrets:\n', regrets, '\n')

    # Calculate Max regrets vector
    max_regret_st = []
    for s in regrets:
        max_regret_st.append(min(s['st']))

    print('Vector of Maximum regrets for every scenario:\n', max_regret_st)