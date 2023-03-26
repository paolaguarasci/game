from copy import deepcopy

import const


def sortDictByValues(passedDict):
    return {key: val for key, val in sorted(passedDict.items(), key=lambda ele: ele[1], reverse=True)}

def checkDistancesCoerency(dist):
    distances = deepcopy(dist)
    placeChecked = []
    for place in distances:
        placeChecked.append(place)
        for otherPlace in distances[place]:
            if otherPlace not in placeChecked:
                print(place, otherPlace, end="\t")
                d1 = distances[place][otherPlace]
                d2 = distances[otherPlace][place]
                if d1 == d2:
                    print("OK")
                else:
                    print("The two distances", d1, "and", d2, "are different")

def printInfo(net, auctions):
    print("\n")
    totalPayment = 0
    for location in list(auctions.keys()):
        print(location, "--- winner", auctions[location]['winner'].name, "--- payment", auctions[location]['winner'].payment)
        totalPayment += auctions[location]['winner'].payment
    tour = net.findShortestPathBetweenAllSelectedLocations(list(auctions.keys()))
    totalTourCost = tour[1] * const.KMFIXEDCOST + const.FIXEDTOURCOST
    print("\nTotal payments:", totalPayment, "Total tour cost:", totalTourCost, "Differenza: ", totalPayment - totalTourCost)
    # net.printGraph(net.cityNetwork, tour[0])

