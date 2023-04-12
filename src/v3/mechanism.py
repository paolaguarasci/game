import warnings
from copy import deepcopy

import const
import utils
from agent import Agent
from graph import CityNetwork

warnings.filterwarnings("ignore", message="Gtk-Message")

nAgents = 3
agents = []
postiInMacchina = const.MAXUSERFORTOUR

for i in range(0,nAgents):
    agents.append(Agent(str(i)))
    print(agents[i].name, agents[i].utilities)

cityNet = CityNetwork()

def calculateAgentPayment(agent, locations, originalCost):
    totalTourCost = deepcopy(originalCost)
    newAgents = deepcopy(agents)
    newAgents1 = [item for item in newAgents if item.name != agent[0].name]
    newLocation = selectLocationByAgentUtility(newAgents1, const.PLACES)
    newLocation = removeUtilsNull(newLocation)
    print("newLocation ", newLocation)
    newLocationsSorted = list(newLocation.keys())
    
    print("newLocationsSorted ", newLocationsSorted)
    newCycle, newCost = cityNet.findShortestPathBetweenAllSelectedLocations(newLocationsSorted)
    payment = ((totalTourCost - newCost) * const.KMFIXEDCOST) # sarebbe la differenza di km per il costo fisso
    return (payment, newLocationsSorted)

def calculateTotalPayments(agents, locations, cost):
    res = []
    for agent in agents:
        payment, chooseLocation = calculateAgentPayment(agent, locations, cost)
        res.append((agent[0].name, payment, chooseLocation))
    return res

def selectLocationByAgentUtility(agents, locations):
    locations_utilities = dict()
    for location in locations:
        locations_utilities[location] = 0;

    for agent in agents:
        uv = agent.utilities
        for v in uv:
            locations_utilities[v] += uv[v]
    return utils.sortDictByValues(locations_utilities)

def choiceLocationWithLimit(locations, limits):
    res = []
    res.append(locations[0])
    locations.pop(0)
    tripCost = None
    tripCycle = None
    for location in locations:
        res.append(location)
        cycle, cost = cityNet.findShortestPathBetweenAllSelectedLocations(res)
        if cost > limits:
            res.remove(location)
            tripCycle, tripCost = cityNet.findShortestPathBetweenAllSelectedLocations(res)
            break
    return (res, tripCycle, tripCost) 

def choiceAgentsToTrip(agents, locations, limits):
    res = []
    k = 0
    x = 0
    for i in range(0, limits):
        if len(res) > limits:
            break
        res.append(getSpecificValForLocation(agents, locations[k % len(locations)][0], x))
        if (len(res) % len(locations) == 0):
           x += 1
        k += 1
    return res

def getSpecificValForLocation(agents, location, nval):
    val = []
    for agent in agents:
        uvals = agent.utilities
        uval = uvals[location]
        val.append((uval, agent))
    val.sort(key = lambda i:i[0], reverse = True)
    return (val[nval][1], location)

def fixSharePayments(tourLocations, pays):
    payments = deepcopy(pays)
    payments = sorted(payments, key=lambda x: x[2])
    res = []
    for city in tourLocations:
        filteredByCity = list(filter(lambda x: x[2] == city, payments))
        if len(filteredByCity) > 1:
             for x in filteredByCity:
                xl = list(x)
                xl[1] /= len(filteredByCity)
                res.append(tuple(xl))
        else:
            res.append(filteredByCity)
    return res

def removeUtilsNull(loc):
    backupLoc = deepcopy(loc)
    res = {key:val for key, val in backupLoc.items() if val != 0}
    return res;

sumOfUtilities = selectLocationByAgentUtility(agents, const.PLACES)
locationsSorted = list(sumOfUtilities.keys())

# Non si sta prendendo la citta' di partenza
# locationsSorted.insert(0, const.STARTPLACE)

locationLimitated, cycle, cost = choiceLocationWithLimit(locationsSorted, const.MAXKMFORTOUR)
tourCost = cost * const.KMFIXEDCOST + const.FIXEDTOURCOST
sumOfValuationChoisedCity = list(filter(lambda x: x[0] in locationLimitated, sumOfUtilities.items()))
sumOfValuationChoisedCity.append((const.STARTPLACE, 0))
agentsInCar = choiceAgentsToTrip(agents, sumOfValuationChoisedCity, const.MAXUSERFORTOUR)

print("sumOfUtilities", sumOfUtilities)
print("locationsSorted", locationsSorted)
print("locationLimitated", locationLimitated)
print("locationLimitated cycle", cycle)
print("locationLimitated cost", cost)
print("sumOfValuationChoisedCity ", sumOfValuationChoisedCity)
print("agentsInCar", agentsInCar)

payments1 = calculateTotalPayments(agentsInCar, locationLimitated, cost)
print("Pagementi variabili ", payments1)
payments2 = fixSharePayments(locationLimitated, payments1)
print("Quote fisse ", payments2)

cityNet.printGraph(cityNet.cityNetwork, cycle)