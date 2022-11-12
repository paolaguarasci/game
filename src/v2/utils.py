from copy import deepcopy
from random import randint


def sortDictByValues(passedDict):
    return {key: val for key, val in sorted(passedDict.items(), key=lambda ele: ele[1], reverse=True)}


def genRandomUtilitiesSorted(places):
    utilities = [randint(-3, 4) for i in range(len(places), 0, -1)]
    placesToBeValuate = deepcopy(places)
    userUtilities = {}
    for utility in utilities:
        place = placesToBeValuate[randint(0, len(placesToBeValuate)-1)]
        placesToBeValuate.remove(place)
        userUtilities[place] = utility
    return sortDictByValues(userUtilities)


def genRandomMaxPayments():
    # TODO Aggiunstare questi valori
    return randint(1, 10)


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
