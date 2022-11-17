from scipy.stats.distributions import nakagami
import networkx as nx
import matplotlib.pyplot as plt
import random


# (a)
def erdos_renyi(n, p):
    G = nx.Graph()
    my_nodes = list(x for x in range(0, n))
    num_of_edges = 0
    for n1 in my_nodes:
        G.add_node(n1)
        for n2 in my_nodes:
            if n1 > n2:
                rand = random.uniform(0, 1)
                if rand <= p:
                    G.add_edge(n1, n2)
                    num_of_edges += 1

    plt.figure(3, figsize=(26, 15))
    nx.draw(G, with_labels=True, node_size=3000, node_color="skyblue", font_size=30)
    plt.show()
    return G


# (b)
def node_clustering_coefficient(G, node):
    k = G.degree(node)
    if k == 0 or k == 1:
        return 0
    neighbors = G[node]
    neighbors_edges = 0
    for n1 in neighbors:
        for n2 in neighbors:
            if n1 != n2 and (n1, n2) in G.edges:
                neighbors_edges += 1
    neighbors_edges = neighbors_edges / 2
    return (2 * neighbors_edges) / (k * (k - 1))


# TODO: VERIFY THE AVG
def graph_clustering_coefficient(G):
    n = len(G.nodes)
    sum_coeff = 0
    for node in G.nodes:
        sum_coeff += node_clustering_coefficient(G, node)
    return sum_coeff / n


