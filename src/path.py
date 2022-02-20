"""
  GOAL 
  - selezionare gli utenti che eseguiranno il tour
  - deve definire i luoghi che verranno visitati dal tour
  - deve definire i pagamenti che vengono addebitati agli utenti

  VINCOLI
  - A nessun utente deve essere addebitato un costo maggiore rispetto
    a quello che e' disposto a pagare (max)

  NICE TO HAVE
  - il costo del tour, che e' proporzionale alla lunghezza in km, 
    deve essere equamente distribuito tra gli utenti del veicolo, 
    in modo che nessun agente abbia argomenti per opporsi.
  - il costo fisso deve essere ripartito tra gli agenti in base 
    alle utilita' dichiarate, e attuando meccanismi che portino a 
    dichiarare in modo veritiero le utilita'.
"""

from importlib.resources import path
from random import randrange
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import approximation as approx

# https://networkx.org/documentation/latest/reference/algorithms/shortest_paths.html

G = nx.DiGraph()

G.add_weighted_edges_from({
    (1, 2, 3),    (1, 3, 17),   (1, 4, 14),   (1, 5, 11),   (1, 6, 8),
    (2, 1, 3),    (2, 3, 12),   (2, 4, 16),   (2, 5, 10),   (2, 6, 6),
    (3, 1, 13),   (3, 2, 12),   (3, 4, 4),    (3, 5, 7),    (3, 6, 5),
    (4, 1, 14),   (4, 2, 15),   (4, 3, 2),    (4, 5, 9),    (4, 6, 3),
    (5, 1, 14),   (5, 2, 15),   (5, 3, 2),    (5, 4, 9),    (5, 6, 3),
    (6, 1, 14),   (6, 2, 15),   (6, 3, 2),    (6, 4, 9),    (6, 5, 3)
})


def printGraph(graph):
  pos = nx.nx_pydot.pydot_layout(G)
  options = {
      "font_size": 16,
      "node_size": 1500,
      "node_color": "white",
      "edgecolors": "black",
      "linewidths": 3,
      "width": 3,
  }
  nx.draw_networkx(graph, pos, **options)
  nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, "weight"), font_size=12, rotate=False)
  ax = plt.gca()
  ax.margins(0.20)
  plt.axis("off")
  plt.show()

def findPath(graph):
    cycle = approx.greedy_tsp(graph, weight="weight")
    try:
      cost = sum(graph[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle))
    except:
      cost = 0
    return cost

def genUsers(numUsers):
  users = []
  for i in range(numUsers):
    loc = randrange(1, 7)
    util = randrange(1, 100)
    max = randrange(1, 25)
    users.append((loc, util, max))
  return users

def calcoloCostoFisso():
  pass

users = genUsers(20)
maxUsersInCar = 5
lenMax = 100
fixCost = 10
kmCost = 1.5 

location = set()
travellers = set()

for user in users:
  if len(travellers) < maxUsersInCar:
    tmpLocation = location.copy()
    tmpLocation.add(user[0])
    subg = nx.subgraph(G, tmpLocation)
    lenKm = findPath(subg)
    travelCost = float(lenKm * kmCost) / (len(travellers) + 1)
    if (lenKm <= lenMax) and travelCost < user[2]:
      location.add(user[0])
      travellers.add(user)
      for u in users:
        if u[2] < travelCost:
          travellers.discard(u)
          o = [user for user in travellers if user[0] == u[0]]
          if len(o) == 0:
            location.discard(u[0])
          
        

print(travellers)
print(location)

totalCost = findPath(nx.subgraph(G, location)) * kmCost

print("Num Viaggiatori: ", len(travellers))
print("Costo viaggio: ", totalCost)
print("Costo viaggio pro capite: ", totalCost / len(travellers))

printGraph(G)
printGraph(nx.subgraph(G, location))