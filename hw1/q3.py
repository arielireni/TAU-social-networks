import networkx as nx


def get_all_triples(G):
    nodes = list(G.nodes)
    triples = []
    for i in range(0, len(nodes)-2):
        for j in range(i+i, len(nodes)-1):
            for k in range(j+1, len(nodes)):
                triples.append((nodes[i], nodes[j], nodes[k]))

    return triples


def get_all_triangles(G):
    edges = list(G.edges)
    triples = get_all_triples(G)
    triangles = []
    for triple in triples:
        if (triple[0], triple[1]) in edges or (triple[1], triple[0]) in edges:
            if(triple[2], triple[1]) in edges or (triple[1], triple[2]) in edges:
                if(triple[0], triple[2]) in edges or (triple[2], triple[0]) in edges:
                    triangles.append(triple)
    return triangles


def check_balance(G):
    triangles = get_all_triangles(G)
    edge_labels = dict([((u, v), d['label']) for u, v, d in G.edges(data=True)])
    for triangle in triangles:
        count_minus = 0
        if (triangle[0], triangle[1]) in edge_labels.keys() and edge_labels[(triangle[0], triangle[1])] == '-':
            count_minus += 1
        if (triangle[1], triangle[0]) in edge_labels.keys() and edge_labels[(triangle[1], triangle[0])] == '-':
            count_minus += 1

        if (triangle[0], triangle[2]) in edge_labels.keys() and edge_labels[(triangle[0], triangle[2])] == '-':
            count_minus += 1
        if (triangle[2], triangle[0]) in edge_labels.keys() and edge_labels[(triangle[2], triangle[0])] == '-':
            count_minus += 1

        if (triangle[2], triangle[1]) in edge_labels.keys() and edge_labels[(triangle[2], triangle[1])] == '-':
            count_minus += 1
        if (triangle[1], triangle[2]) in edge_labels.keys() and edge_labels[(triangle[1], triangle[2])] == '-':
            count_minus += 1

        if count_minus % 2 == 1:
            return False
    return True


def test():
    G=nx.DiGraph()
    # Add nodes by specifying their positions
    G.add_node('10', pos=(2, 10))
    G.add_node('9',  pos=(4, 9))
    G.add_node('8',  pos=(0, 13))
    G.add_node('7',  pos=(1.5, 4))
    G.add_node('6',  pos=(4, 4))
    G.add_node('5',  pos=(6, 11))
    G.add_node('3',  pos=(6, 6))
    G.add_node('0',  pos=(0, 0))
    # Add edges by defining weight and label
    G.add_edge('10','9',weight=1, label='+')
    G.add_edge('10','8',weight=1, label='-')
    G.add_edge('10','7',weight=1, label='-')
    G.add_edge('9','3', weight=1, label='+')
    G.add_edge('9','6',weight=1, label='+')
    G.add_edge('9','5',weight=1, label='+')
    G.add_edge('7','0',weight=1, label='+')
    G.add_edge('7','6',weight=0, label='-')
    G.add_edge('6','3',weight=0, label='-')
    G.add_edge('5','3',weight=0, label='-')
    print(check_balance(G))
