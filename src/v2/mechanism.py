import const
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
