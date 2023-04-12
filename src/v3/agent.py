import math
from copy import deepcopy
from random import randint

import const
from utils import sortDictByValues


class Agent():
  name = None
  utilities = None
  max_payments = None

  def __init__(self, name) -> None:
    self.name = "Agent" + name
    self.max_payments = self.randomize_max_payment()
    self.utilities = self.gen_random_utilities_sorted(const.PLACES)

  def randomize_max_payment(self):
    return randint(500, 1000)
  
  def gen_random_utilities_sorted(self, places):
    utilities = range(0, len(places))
    places_to_be_valuate = deepcopy(places)
    user_utilities = {}
    for utility in utilities:
        place = places_to_be_valuate[randint(0, len(places_to_be_valuate)-1)]
        places_to_be_valuate.remove(place)
        user_utilities[place] = utility
    return sortDictByValues(user_utilities)

  def __str__(self):
    return self.name

  def __repr__(self):
    return self.__str__()