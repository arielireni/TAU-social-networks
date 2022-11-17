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
    return


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
