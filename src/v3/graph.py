from copy import deepcopy

import const
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import approximation as approx


class CityNetwork():
    cityNetwork = None
    locations = None
    
    def __init__(self, pesi) -> None:
        self.cityNetwork = nx.Graph()
        if not pesi:
            self.cityNetwork.add_weighted_edges_from(self.generateWeightedEdge(const.DISTANCES))
        else:
            self.cityNetwork.add_weighted_edges_from(self.generateWeightedEdge(pesi))
    
    
    def generateWeightedEdge(self, dist):
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

    def printGraph(self, graph, path=None):
        pos = nx.circular_layout(self.cityNetwork)
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
        nx.draw_networkx_labels(graph, pos, bbox=label_options)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(
            graph, "weight"), font_size=12, rotate=True)
        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()

        if path:
            edge_list = list(nx.utils.pairwise(path, cyclic=True))
            nx.draw_networkx(graph,pos,with_labels=True,edgelist=edge_list,edge_color="red",node_size=200,width=3)

        plt.show()


    def filter_node(self, n1):
        return n1 in self.locations

    def creteSubGraph(self):
        return nx.subgraph_view(self.cityNetwork, filter_node=self.filter_node)

    def findShortestPathBetweenAllSelectedLocations(self, locations):
        self.locations=locations
        subView = self.creteSubGraph()
        cycle = approx.greedy_tsp(subView, weight="weight")
        cost = sum(self.cityNetwork[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle))
        return (cycle, cost)

    def findDistanceToNoSelectedLocations(self, locations):
        self.locations=locations
        distances, path = nx.multi_source_dijkstra(self.cityNetwork, locations)
        return (distances, path)

