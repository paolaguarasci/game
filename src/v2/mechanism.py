import const
import graph
import utils

agents = [{
    "name": "u1",
    "utilities": {},
    "maxPayments": None
},
    {
    "name": "u2",
    "utilities": {},
    "maxPayments": None
},
    {
    "name": "u3",
    "utilities": {},
    "maxPayments": None
},
    {
    "name": "u4",
    "utilities": {},
    "maxPayments": None
},
    {
    "name": "u5",
    "utilities": {},
    "maxPayments": None
}
]

# Preparazione agenti - generazione random di utilities e pagamento massimo
for agent in agents:
    agent["utilities"] = utils.genRandomUtilitiesSorted(const.PLACES)
    agent["maxPayments"] = utils.genRandomMaxPayments()
    print(agent)


# mi serve una funzione che dato un grafo riesca a calcolare il best path in assoluto
# questa stessa funzione dovrebbe riuscire a calcolare anche il best path di un sottografo (che resta cmq un grafo)
# ho cosi la differenza tra best path in assoluto e best path senza l'utente i
# posso costruire il pagamento di conseguenza


"""
### Obiettivo:
- Il sistema deve:
    - selezionare gli utenti che eseguiranno il tour
    - definire i luoghi che saranno visitati dal tour
    - definire i pagamenti che vengono addebitati agli utenti.

### Vincolo:
- A nessun utente può essere addebitato un importo superiore al pagamento massimo che ha dichiarato.

### Desiderata:
- Il costo del tour, che è proporzionale alla lunghezza in km, deve essere equamente distribuito tra gli utenti del veicolo, 
in modo che nessun agente abbia argomenti per opporsi.
- Il costo fisso deve essere distribuito tra gli agenti in base alle utilità dichiarate, 
e implementando un meccanismo che porti a dichiarare in modo veritiero le utilità.
"""

graph.printGraph(graph.G)
locations = ["rome", "berlin", "vienna", "brussels"]
cycle = graph.approx.christofides(graph.G, weight="weight")
subGraph = graph.nx.subgraph(graph.G, cycle)
graph.printGraph(graph.G, subGraph)