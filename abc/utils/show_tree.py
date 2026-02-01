import networkx as nx
import matplotlib.pyplot as plt

def main():
    N, M = map(int, input().split())

    G = nx.MultiGraph()
    G.add_nodes_from(range(1, N + 1))

    for _ in range(M):
        u, v = map(int, input().split())
        G.add_edge(u, v)

    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, node_size=600, node_color='lightblue')
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)

    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
