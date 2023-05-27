import warnings
from copy import deepcopy

import const
import utils
from agent import Agent
from graph import CityNetwork

from itertools import chain, combinations

warnings.filterwarnings("ignore", message="Gtk-Message")
DEBUG=True
nAgents = 2 # Paola e Francesca
agentsName = ["Paola", "Francesca"]
agents = []
postiInMacchina = const.MAXUSERFORTOUR

for i in range(0,nAgents):
    agents.append(Agent(agentsName[i]))
    print(agents[i].name, agents[i].utilities)

cityNet = CityNetwork()

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# Calcolo di ogni possibile tour e del costo relativo
def calculateAllTourWithCost(locations):
    powerSetLocations = powerset(locations)
    # rimozione tour che non hanno la citta' i partenza tra le citta' contemplate
    filtered1 = filter(lambda x: const.STARTPLACE in x, powerSetLocations)
    # rimozione tour di dimensione 0 e 1
    filtered2 = filter(lambda x: len(x) > 1, filtered1)
    
    filterdWithCost = []
    
    for tour in filtered2:
        cycle, cost = cityNet.findShortestPathBetweenAllSelectedLocations(tour)
        filterdWithCost.append((tour, cost))
    
    return sorted(filterdWithCost, key=lambda tup: tup[1], reverse=True)

# Rimozione dei tour che superano il limite kilometrico
def removeTourOverKMLimit(location,limits):
    return list(filter(lambda tup: tup[1] < limits, location))

# Calcolo delle utilita' di ogni tour
def calculateUtilityForAllTour(tours, agents):
    res = []
    for tour in tours:
        tourUtility = 0
        for agent in agents:
            for city in tour[0]:
                if city != const.STARTPLACE:
                    tourUtility += agent.getUtility(city)
        res.append((tour[0], tourUtility))
    return sorted(res, key=lambda tup: tup[1], reverse=True)

# Calcolo del costo del tour per ogni agente
def calculateAgentPayment(selectedTour, agent):
    agentInterest = agent.getCityMaxUtility(selectedTour)
    # TODO Risolvere questo problema in qualche modo!!!
    # Attenzione in 
    # 'cityNet.findShortestPathBetweenAllSelectedLocations(agentInterest)'
    # la lista di location agentInterest deve avere lunghezza almeno pari a 2
    if len(agentInterest) > 1:
        _, costoCompleto = cityNet.findShortestPathBetweenAllSelectedLocations(selectedTour)
        _, costoSenzaAgente = cityNet.findShortestPathBetweenAllSelectedLocations(selectedTour)
        _, costoPerCuiPartecipa = cityNet.findShortestPathBetweenAllSelectedLocations(agentInterest)
        agent.kmTrattaInteresse = costoPerCuiPartecipa
        costo = costoSenzaAgente - costoPerCuiPartecipa
        # TODO decidere cosa fare se non supera il budget
        return (costo, agent.budget < costo)
    return (0, False)

# Calcolo l'incasso totale del meccanismo come somma dei pagamenti dei singoli agenti
def calcoloIncassoTotale(selectedTour, agents):
    costoTotale = 0
    for agent in agents:
        pagamentoAgente = calculateAgentPayment(selectedTour[0], agent)
        agent.pagamento = pagamentoAgente[0]
        costoTotale += pagamentoAgente[0]
        print(agent.name, pagamentoAgente)
    return costoTotale

def calcoloScontoEPagamentoFinale(agent, costoAlKm):
    if agent.kmTrattaInteresse and agent.kmTrattaInteresse > 0:
        agent.sconto = costoAlKm * agent.kmTrattaInteresse
        print("Sconto", agent.sconto)
        agent.pagamentoFinale = agent.pagamento - agent.sconto
        print("Pagamento finale", agent.pagamentoFinale)
    return agent.pagamentoFinale

def getTourCost(selectedTour):
    _, costo = cityNet.findShortestPathBetweenAllSelectedLocations(selectedTour)
    return costo

allTour = calculateAllTourWithCost(const.PLACES)
if DEBUG: print("\n\nTutti i tour possibili\n", allTour)

allTourCapped = removeTourOverKMLimit(allTour, const.MAXKMFORTOUR)
if DEBUG: print("\n\nTutti i tour possibili che rientrano nel limite dei km max\n", allTourCapped)

allTourCappedWithUtility = calculateUtilityForAllTour(allTourCapped, agents)
if DEBUG: print("\n\nTutti i tour possibili con le relative utility\n", allTourCappedWithUtility)

# possiamo prendere il primo elemento della lista perche' la funzione di 
# calcolo 'calculateUtilityForAllTour' restituisce una lista ordinata per utilita'
# in ordine inverso. Il primo elemento della lista quindi massimiza l'utilita'
selectedTour = allTourCappedWithUtility[0]
if DEBUG: print("\n\nTour selezionato (massimizza utlita')\n", selectedTour)

# citta' di interesse degli agenti all'interno del tour selezionato:
if DEBUG: 
    print("\n\nInteresse degli agenti")
    for agent in agents:
        print(agent.name, agent.getCityMaxUtility(selectedTour[0]))

incassoTotale = calcoloIncassoTotale(selectedTour, agents)
if DEBUG: print("\n\nIncasso totale\n", incassoTotale)

costoRealeTour = getTourCost(selectedTour[0]) # in termini di km
surplus = incassoTotale - costoRealeTour # <- qui non va bene questo valore, e' in km, non possiamo sottrarli ai soldi!
if DEBUG: print("\n\nSurpluss\n", surplus)

costoAlKm = surplus / costoRealeTour
if DEBUG: print("\n\nCosto per km\n{:.2f}".format(costoAlKm))


if DEBUG: 
    print("\n\nCalcolo sconti e pagamento finale")
    for agent in agents:
        print(agent.name, calcoloScontoEPagamentoFinale(agent, costoAlKm))

# cityNet.printGraph(cityNet.cityNetwork, cycle)