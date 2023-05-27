import math
from copy import deepcopy
from random import randint

import const
from utils import sortDictByValues


class Agent():
  name = None
  utilities = None
  budget = None
  pagamento = None
  pagamentoFinale = None
  sconto = None
  kmTrattaInteresse = None

  def __init__(self, name) -> None:
    self.name = name
    self.budget = self.randomize_budget()
    self.utilities = self.gen_random_utilities_sorted(const.PLACES)

  def randomize_budget(self):
    return randint(450, 550)
  
  def gen_random_utilities_sorted(self, places):
    utilities = range(0, len(places)-1)
    places_to_be_valuate = deepcopy(places)
    places_to_be_valuate.remove(const.STARTPLACE)
    user_utilities = {}
    for utility in utilities:
        place = places_to_be_valuate[randint(0, len(places_to_be_valuate)-1)]
        places_to_be_valuate.remove(place)
        user_utilities[place] = utility
    return sortDictByValues(user_utilities)

  def getUtility(self, city):
    return self.utilities[city]
  
  # Dato un tour restituisce una lista di citta' di interesse per l'agente 
  # (cioe' con utilita' maggiore di 0)
  def getCityMaxUtility(self, tour):
    res = []
    for city in tour:
      if (city != const.STARTPLACE and self.utilities[city] > 0):
        res.append(city)
    return res
  
  def __str__(self):
    return self.name

  def __repr__(self):
    return self.__str__()