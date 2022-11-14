import math
from copy import deepcopy
from random import randint

import const
from utils import sortDictByValues


class Agent():
  name = None
  utilities = None
  valuations = None
  maxPayments = None

  def __init__(self, name) -> None:
    self.name = "Agent " + name
    self.utilities = self.genRandomUtilitiesSorted(const.PLACES)
    self.maxPayments = self.genRandomMaxPayments()
    self.valuations = self.genRandomValuationsSorted()

  def genRandomUtilitiesSorted(self, places):
    # utilities = [randint(-3, 4) for i in range(len(places), 0, -1)]
    utilities = range(0, len(places))
    placesToBeValuate = deepcopy(places)
    userUtilities = {}
    for utility in utilities:
        place = placesToBeValuate[randint(0, len(placesToBeValuate)-1)]
        placesToBeValuate.remove(place)
        userUtilities[place] = utility
    return sortDictByValues(userUtilities)

  def genRandomValuationsSorted(self):
      vals = []
      for util in self.utilities:
          val = math.floor((self.maxPayments / 7) * self.utilities[util]);
          vals.append((util, val))
      vals.sort(key=lambda a: a[1], reverse = True)
      return vals

  def genRandomMaxPayments(self):
      # TODO Aggiustare questi valori (il costo massimo e' circa 12000)
      return randint(7000, 12000)
  
  def getFirstValuation(self):
    return self.valuations[0]
  
  def getValutations(self):
    return self.valuations

  def getName(self): 
    return self.name

  def __str__(self):
    return self.name

  def __repr__(self):
    return self.__str__()