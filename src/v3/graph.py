from copy import deepcopy

import const
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import approximation as approx


class CityNetwork():
    cityNetwork = None
    locations = None
    initialWeight = None
    
    def __init__(self, pesi) -> None:
        self.cityNetwork = nx.Graph()
        self
        if not pesi:
            self.cityNetwork.add_weighted_edges_from(self.generateWeightedEdge(const.DISTANCES))
            self.initialWeight = const.DISTANCES
        else:
            self.cityNetwork.add_weighted_edges_from(self.generateWeightedEdge(pesi))
            self.initialWeight = pesi
    
    
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

    def findAlternative(self, locations):
        edge = self.cleanEdgeV2(self.initialWeight, locations)
        tempGraph = nx.DiGraph()
        tempGraph.add_weighted_edges_from(self.generateWeightedEdge(edge))
        cycle = nx.shortest_path(tempGraph, source=locations[0], target=locations[len(locations)-1], weight="weight", method='dijkstra')
        costAndata = nx.shortest_path_length(tempGraph, source=locations[0], target=locations[len(locations)-1], weight="weight", method='dijkstra')
        costRitorno = nx.shortest_path_length(tempGraph, source=locations[len(locations)-1], target=locations[0], weight="weight", method='dijkstra')
        return (cycle, costAndata+costRitorno)

    def findAlternativeAB(self, locations, a, b):
        edge = self.cleanEdgeV2(self.initialWeight, locations)
        tempGraph = nx.DiGraph()
        tempGraph.add_weighted_edges_from(self.generateWeightedEdge(edge))
        cycle = nx.shortest_path(tempGraph, source=a, target=b, weight="weight", method='dijkstra')
        cost = nx.shortest_path_length(tempGraph, source=a, target=b, weight="weight", method='dijkstra')
        return (cycle, cost)

    def findDistanceToNoSelectedLocations(self, locations):
        self.locations=locations
        distances, path = nx.multi_source_dijkstra(self.cityNetwork, locations)
        return (distances, path)

    def cleanEdge(self, edgeList, tour):
        localCopy = deepcopy(edgeList)
        keyArr = deepcopy(list(localCopy.keys()))
        for key in keyArr:
            if key not in tour:
                del localCopy[key]
            else:
                lv2keyArr = deepcopy(list(localCopy[key].keys()))
                for key1 in lv2keyArr:
                    if key1 not in tour:
                        del localCopy[key][key1]
        return localCopy  
    
    def cleanEdgeV2(self, edgeList, tour):
        res = {}
        localCopy = deepcopy(edgeList)
        localTour = list(deepcopy(tour))
        keyArr = deepcopy(list(localCopy.keys()))
        if localTour[len(localTour)-1] != const.STARTPLACE:
            localTour.append(const.STARTPLACE)
        if localTour[0] != const.STARTPLACE:
            localTour.insert(0, const.STARTPLACE)
            
        for idx, val in enumerate(localTour):
            if idx < len(localTour)-1:
                if localTour[idx] not in res.keys():
                    res[localTour[idx]] = {}
                res[localTour[idx]][localTour[idx+1]] = edgeList[localTour[idx]][localTour[idx+1]]
        return res
        
    def cleanEdgeV3(self, edgeList, edges):
        res = {}
        localCopy = deepcopy(edgeList)
        for edge in edges:
            if edge[0] not in res.keys():
                res[edge[0]] = {}
            print(edge[0], edge[1])
            res[edge[0]][edge[1]] = localCopy[edge[0],edge[1]]
        return res