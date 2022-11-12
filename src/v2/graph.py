from copy import deepcopy

import const
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import approximation as approx

G = nx.Graph()


def generateWeightedEdge(dist):
    distances = deepcopy(dist)
    edges = list()
    placeChecked = []
    for place in distances:
        placeChecked.append(place)
        for otherPlace in distances[place]:
            if otherPlace not in placeChecked:
                d1 = distances[place][otherPlace]
                edges.append((place, otherPlace, d1))
    return edges


G.add_weighted_edges_from(generateWeightedEdge(const.DISTANCES))


def printGraph(graph, path=None):
    pos = nx.circular_layout(G)
    options = {
        "font_size": 0,
        "node_size": 12,
        "font_color": "black",
        "font_weight": "800",
        "linewidths": 3,
        "width": 3,
    }
    nx.draw_networkx(graph, pos, **options)
    label_options = {"ec": "k", "fc": "white", "alpha": 0.7}
    nx.draw_networkx_labels(graph, pos, bbox=label_options);
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(
        graph, "weight"), font_size=12, rotate=True)
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()

    if path:
        edge_list = list(nx.utils.pairwise(path))
        nx.draw_networkx(graph,pos,with_labels=True,edgelist=edge_list,edge_color="red",node_size=200,width=3)
    
    plt.show()


def findPath(graph):
    cycle = approx.greedy_tsp(graph, weight="weight")
    try:
        cost = sum(graph[n][nbr]["weight"]
                   for n, nbr in nx.utils.pairwise(cycle))
    except:
        cost = 0
    return cost


