import warnings
from copy import deepcopy

import const
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

agentsValuation = []
for agent in agents:
    l, v = agent.getFirstValuation()
    agentsValuation.append((l, v, agent.getName()))
agentsValuation.sort(key=lambda x: (x[0], -x[1]))
print(agentsValuation)

locations = set()
for agentValuation in agentsValuation:
    locations.add(agentValuation[0])
cycle, cost = cityNet.findShortestPathBetweenAllSelectedLocations(locations)
cityNet.printGraph(cityNet.cityNetwork, cycle)

while cost > const.MAXKMFORTOUR:
    print("WARNING: The tour has to many KM")
    locations.pop()
    cycle, cost = cityNet.findShortestPathBetweenAllSelectedLocations(locations)

cityNet.printGraph(cityNet.cityNetwork, cycle)

filteredAgents = []

for place in locations:
    offers = list(filter(lambda x: x[0] == place, agentsValuation))
    offers.sort(key=lambda x: x[1])
    agent = list(filter(lambda x: x.getName() == offers[0][2], agents))
    filteredAgents.append(agent[0])

print(filteredAgents)

distances, path = cityNet.findDistanceToNoSelectedLocations(locations)
totalCostTour = const.FIXEDTOURCOST + (cost * const.KMFIXEDCOST)
distancesToOtherPlace = dict(filter(lambda val: val[1] > 0, distances.items()))

print("Selected Locations: ", list(locations))
print("Distance to other places: ", distancesToOtherPlace)
print("Lenght (KM) of shortest path: ", cost)
print("Total tour price: ", totalCostTour)

cityNet.printGraph(cityNet.cityNetwork, cycle)

def placesThatMaximizeValuation():
    places = []
    return places

def calculateAgentPayment(agent, locations, originalCost):
    totalTourCost = deepcopy(originalCost)
    originalLocations = deepcopy(locations)
    chooseLocation = agent.getFirstValuation()[0]
    originalLocations.remove(chooseLocation)
    newCycle, newCost = cityNet.findShortestPathBetweenAllSelectedLocations(originalLocations)
    payment = ((totalTourCost - newCost) * const.KMFIXEDCOST)
    # print(agent.getName(), end="\t")
    # print(chooseLocation, end="\t")
    # print("payment request: ", payment)
    # cityNet.printGraph(cityNet.cityNetwork, newCycle)
    return (payment, chooseLocation)

payments = []
totalOfPayments = 0

placeVote = dict()
for place in const.PLACES:
    placeVote[place] = 0

for agent in filteredAgents:
    place, valuation = agent.getFirstValuation()
    placeVote[place] += 1

print(placeVote)

for agent in filteredAgents:
    payment, chooseLocation = calculateAgentPayment(agent, locations, cost)
    totalOfPayments += payment
    payments.append((agent.getName(), payment, chooseLocation))

print(payments)
print("Total payments:", totalOfPayments, "Total cost: ", totalCostTour)

if len(filteredAgents) > const.MAXUSERFORTOUR:
    print("WARNING: The tour has to many users")