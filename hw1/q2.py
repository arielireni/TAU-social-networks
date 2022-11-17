from scipy.stats.distributions import nakagami
import networkx as nx
import matplotlib.pyplot as plt
import random


def degree_centrality(G):
    n = len(G.nodes)
    return {node: (G.degree(node) / (n - 1)) for node in G.nodes}


def betweenness_centrality(G):
    n = len(G.nodes)
    betweennes_dict = dict()
    for node_i in G.nodes:
        count_i_in_path = 0
        for node_s in G.nodes:
            for node_t in G.nodes:
                if node_i != node_s and node_s != node_t and node_t != node_i:
                    all_shortest_paths = list(nx.all_shortest_paths(G, node_s, node_t))
                    for path in all_shortest_paths:
                        if node_i in path:
                            count_i_in_path += 1

        count_i_in_path = count_i_in_path / 2
        betweennes_dict[node_i] = count_i_in_path * (2 / ((n - 1) * (n - 2)))
    return betweennes_dict


def closeness_centrality(G):
    n = len(G.nodes)
    closeness_dict = dict()
    for n1 in G.nodes:
        curr_sum = 0
        for n2 in G.nodes:
            if n1 != n2:
                curr_sum += nx.shortest_path_length(G, n1, n2)

        closeness_dict[n1] = (n - 1) * (1 / curr_sum)
    return closeness_dict


def create_graph(n=15, p=0.5):
    G = nx.Graph()
    my_nodes = list(x for x in range(0, n))
    for n1 in my_nodes:
        G.add_node(n1)
        for n2 in my_nodes:
            if n1 > n2:
                rand = random.uniform(0, 1)
                if rand <= p:
                    G.add_edge(n1, n2)
    return G

def get_top_5_nodes():
    result = dict()
    G = create_graph()

    Cd_dict = degree_centrality(G)
    Cd_list = [(k, v) for k, v in Cd_dict.items()]
    Cd_list.sort(key=lambda x: x[1])
    Cd_top_5 = Cd_list[-5:]
    result["degree"] = Cd_top_5

    Cb_dict = betweenness_centrality(G)
    Cb_list = [(k, v) for k, v in Cb_dict.items()]
    Cb_list.sort(key=lambda x: x[1])
    Cb_top_5 = Cb_list[-5:]
    result["betweenness"] = Cb_top_5

    Cc_dict = closeness_centrality(G)
    Cc_list = [(k, v) for k, v in Cc_dict.items()]
    Cc_list.sort(key=lambda x: x[1])
    Cc_top_5 = Cc_list[-5:]
    result["closeness"] = Cc_top_5

    return result


def visualize_network():
    G = create_graph(p=0.2)

    Cd_dict = degree_centrality(G)
    Cd_cetralities = list(Cd_dict.values())
    plt.figure(1, figsize=(10, 10))
    nx.draw(G, with_labels=True, node_size=[val*9000 for val in Cd_cetralities], node_color="skyblue", font_size=30)

    Cb_dict = betweenness_centrality(G)
    Cb_cetralities = list(Cb_dict.values())
    plt.figure(2, figsize=(10, 10))
    nx.draw(G, with_labels=True, node_size=[val * 9000 for val in Cb_cetralities], node_color="skyblue", font_size=30)

    Cc_dict = closeness_centrality(G)
    Cc_cetralities = list(Cc_dict.values())
    plt.figure(3, figsize=(10, 10))
    nx.draw(G, with_labels=True, node_size=[val * 9000 for val in Cc_cetralities], node_color="skyblue", font_size=30)

    plt.show()


def test_cetralities():
    G = nx.Graph()
    G.add_node("A")
    G.add_node("B")
    G.add_node("C")
    G.add_node("D")
    G.add_node("E")
    G.add_node("F")
    G.add_node("G")

    G.add_edge("A", "B")
    G.add_edge("A", "C")
    G.add_edge("A", "D")
    G.add_edge("A", "E")
    G.add_edge("A", "F")
    G.add_edge("A", "G")

    Cd = nx.degree_centrality(G)
    Cb = nx.betweenness_centrality(G)
    Cc = nx.closeness_centrality(G)

    for n in G.nodes():
        print(n, "\t", round(Cd[n], 2), "\t", round(Cb[n], 2), "\t", round(Cc[n], 2))

    nx.draw(G, with_labels=True, node_size=1000, node_color="skyblue")
    plt.show()

    print("degree_centrality: ", degree_centrality(G))
    print(Cd == degree_centrality(G))
    print("betweenness_centrality: ", betweenness_centrality(G))
    print(Cb == betweenness_centrality(G))
    print("closeness_centrality: ", closeness_centrality(G))
    print(Cc == closeness_centrality(G))
