import warnings
from copy import deepcopy

import const
import utils
from agent import Agent
from graph import CityNetwork

warnings.filterwarnings("ignore", message="Gtk-Message")

nAgents = 10
agents = []
postiInMacchina = const.MAXUSERFORTOUR

for i in range(0,nAgents):
    agents.append(Agent(str(i)))

cityNet = CityNetwork()

def calculateAgentPayment(agent, locations, originalCost):
    totalTourCost = deepcopy(originalCost)
    originalLocations = deepcopy(locations)
    chooseLocation = agent[1]
    originalLocations.remove(chooseLocation)
    newCycle, newCost = cityNet.findShortestPathBetweenAllSelectedLocations(originalLocations)
    payment = ((totalTourCost - newCost) * const.KMFIXEDCOST)
    return (payment, chooseLocation)

def calculateTotalPayments(agents, locations, cost):
    res = []
    for agent in agents:
        payment, chooseLocation = calculateAgentPayment(agent, locations, cost)
        res.append((agent[0].getName(), payment, chooseLocation))
    return res

def selectLocationByAgentValutation(agents, locations):
    locationsValuations = dict()
    for location in locations:
        locationsValuations[location] = 0;

    for agent in agents:
        uv = agent.getValutations()
        for v in uv:
            locationsValuations[v[0]] += v[1]
    return utils.sortDictByValues(locationsValuations)

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
        uvals = agent.getValutations()
        uval = list(filter(lambda x: x[0] == location, uvals))
        val.append((uval[0][1], agent))
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


sumOfValuation = selectLocationByAgentValutation(agents, const.PLACES)
locationsSorted = list(sumOfValuation.keys())
locationLimitated, cycle, cost = choiceLocationWithLimit(locationsSorted, const.MAXKMFORTOUR)
tourCost = cost * const.KMFIXEDCOST + const.FIXEDTOURCOST
sumOfValuationChoisedCity = list(filter(lambda x: x[0] in locationLimitated, sumOfValuation.items()))
agentsInCar = choiceAgentsToTrip(agents, sumOfValuationChoisedCity, const.MAXUSERFORTOUR)

print("sumOfValuation", sumOfValuation)
print("locationsSorted", locationsSorted)
print("locationLimitated", locationLimitated)
print("locationLimitated cycle", cycle)
print("locationLimitated cost", cost)
print("sumOfValuationChoisedCity ", sumOfValuationChoisedCity)
print("agentsInCar", agentsInCar)

payments1 = calculateTotalPayments(agentsInCar, locationLimitated, cost)
print("payments1", payments1)
payments2 = fixSharePayments(locationLimitated, payments1)
print("payments2", payments2)

cityNet.printGraph(cityNet.cityNetwork, cycle)