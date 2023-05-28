from graph import CityNetwork
import const
from copy import deepcopy


cityNetKm = CityNetwork(const.DISTANCES)
a,b = cityNetKm.findShortestPathBetweenAllSelectedLocations(['roma', 'milano', 'torino'])
print(a, b)
c,d = cityNetKm.findAlternative(a)
print(c, d)

c,d = cityNetKm.findAlternativeAB(a, 'roma', 'torino')
print(c, d)