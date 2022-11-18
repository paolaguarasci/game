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

  city = None
  valuation = None
  payment = None
  utility = None

  def __init__(self, name) -> None:
    self.name = "Agent" + name
    # self.utilities = self.genRandomUtilitiesSorted(const.PLACES)
    # self.valuations = self.genRandomValuationsSorted()
    self.maxPayments = self.randomizeMaxPayment()
    self.setValuation(const.PLACES)
    # self.setUtility()

  def genRandomUtilitiesSorted(self, places):
    utilities = range(0, len(places))
    placesToBeValuate = deepcopy(places)
    userUtilities = {}
    for utility in utilities:
        place = placesToBeValuate[randint(0, len(placesToBeValuate)-1)]
        placesToBeValuate.remove(place)
        userUtilities[place] = utility
    return sortDictByValues(userUtilities)

  def setUtility(self, places, payment):
    #u=v−p
    self.utility = self.valuation - self.payment

  def setValuation(self, places):
    self.city = places[randint(0, len(places)-1)]
    self.valuation = self.maxPayments

  def randomizeMaxPayment(self):
    return randint(7000, 12000) # TODO Limare questi valori...

  def genRandomValuationsSorted(self):
      vals = []
      for util in self.utilities:
          val = math.floor((self.maxPayments / 7) * self.utilities[util]);
          vals.append((util, val))
      vals.sort(key=lambda a: a[1], reverse = True)
      return vals
 
  def getFirstValutation(self):
    return self.valuations[0]
  
  def getValutations(self):
    return self.valuations

  def getName(self): 
    return self.name

  def __str__(self):
    return self.name

  def __repr__(self):
    return self.__str__()