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
# cityNet.printGraph(cityNet.cityNetwork)

# agentsValuation = []
# for agent in agents:
#     l, v = agent.getFirstValuation()
#     agentsValuation.append((l, v, agent.getName()))
# agentsValuation.sort(key=lambda x: (x[0], -x[1]))
# print(agentsValuation)

# locations = set()
# for agentValuation in agentsValuation:
#     locations.add(agentValuation[0])
# cycle, cost = cityNet.findShortestPathBetweenAllSelectedLocations(locations)
# cityNet.printGraph(cityNet.cityNetwork, cycle)

# while cost > const.MAXKMFORTOUR:
#     print("WARNING: The tour has to many KM")
#     locations.pop()
#     cycle, cost = cityNet.findShortestPathBetweenAllSelectedLocations(locations)

# cityNet.printGraph(cityNet.cityNetwork, cycle)

# filteredAgents = []

# for place in locations:
#     offers = list(filter(lambda x: x[0] == place, agentsValuation))
#     offers.sort(key=lambda x: x[1])
#     agent = list(filter(lambda x: x.getName() == offers[0][2], agents))
#     filteredAgents.append(agent[0])

# print(filteredAgents)

# distances, path = cityNet.findDistanceToNoSelectedLocations(locations)
# totalCostTour = const.FIXEDTOURCOST + (cost * const.KMFIXEDCOST)
# distancesToOtherPlace = dict(filter(lambda val: val[1] > 0, distances.items()))

# print("Selected Locations: ", list(locations))
# print("Distance to other places: ", distancesToOtherPlace)
# print("Lenght (KM) of shortest path: ", cost)
# print("Total tour price: ", totalCostTour)

# cityNet.printGraph(cityNet.cityNetwork, cycle)

# def placesThatMaximizeValuation():
#     places = []
#     return places



# payments = []
# totalOfPayments = 0

# placeVote = dict()
# for place in const.PLACES:
#     placeVote[place] = 0

# for agent in filteredAgents:
#     place, valuation = agent.getFirstValuation()
#     placeVote[place] += 1

# print(placeVote)

# for agent in filteredAgents:
#     payment, chooseLocation = calculateAgentPayment(agent, locations, cost)
#     totalOfPayments += payment
#     payments.append((agent.getName(), payment, chooseLocation))

# print(payments)
# print("Total payments:", totalOfPayments, "Total cost: ", totalCostTour)

# if len(filteredAgents) > const.MAXUSERFORTOUR:
#     print("WARNING: The tour has to many users")

##############

def calculateAgentPayment(agent, locations, originalCost):
    totalTourCost = deepcopy(originalCost)
    originalLocations = deepcopy(locations)
    chooseLocation = agent[1]
    originalLocations.remove(chooseLocation)
    newCycle, newCost = cityNet.findShortestPathBetweenAllSelectedLocations(originalLocations)
    payment = ((totalTourCost - newCost) * const.KMFIXEDCOST)
    # print(agent.getName(), end="\t")
    # print(chooseLocation, end="\t")
    # print("payment request: ", payment)
    # cityNet.printGraph(cityNet.cityNetwork, newCycle)
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