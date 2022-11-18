import warnings
from copy import deepcopy
from random import randint

import const
import utils
from agent import Agent
from graph import CityNetwork

nAgents = 250
agents = []
placeInCar = const.MAXUSERFORTOUR
goods = const.PLACES

for i in range(0,nAgents):
    agents.append(Agent(str(i)))

cityNet = CityNetwork()

# Aste al secondo prezzo 
# con beni presi in sequenza
# senza controllo sul prezzo di riserva 
# e senza controllo sul numero max di vincitori
auction0 = dict()
# itero sui beni
for good in goods:
    bidders = list()
    # itero sugli offerenti
    for agent in agents:
        if agent.city == good:
            bidders.append((agent, agent.valuation))
    # ordino le offerte in ordine discendente per valutazione
    bidders.sort(key = lambda i:i[1], reverse = True)
    # l'asta non viene aggiudicata a nessuno se non ci sono almeno due offerenti per lo stesso bene
    if len(bidders) > 2:
        auction0[good] = {
            "winner": bidders[0][0],
            "payment": bidders[1][1]
        }
print("auction0\n", auction0, "\n\n")


# Asta al secondo prezzo 
# con beni presi random
# senza controllo sul prezzo di riserva 
# e senza controllo sul numero max di vincitori
auction1 = dict()
goodsRemained = deepcopy(goods) 
# itero sui beni
for i in range(0, len(goodsRemained)):
    bidders = list()
    # scelgo random una localita' da mettere all'asta
    good = goodsRemained[randint(0, len(goodsRemained)-1)]
    # itero sugli offerenti
    for agent in agents:
        if agent.city == good:
            bidders.append((agent, agent.valuation))
    # ordino le offerte in ordine discendente per valutazione
    bidders.sort(key = lambda i:i[1], reverse = True)
    # l'asta non viene aggiudicata a nessuno se non ci sono almeno due offerenti per lo stesso bene
    if len(bidders) > 2:
        auction1[good] = {
            "winner": bidders[0][0],
            "payment": bidders[1][1]
        }
    goodsRemained.remove(good)
print("auction1\n", auction1, "\n\n")


# Asta al secondo prezzo
# con beni presi random
# senza controllo sul prezzo di riserva 
# con controllo del numero max di vincitori
auction2 = dict()
goodsRemained = deepcopy(goods) 
# itero sui beni
for i in range(0, len(goodsRemained)):
    if len(auction2) < placeInCar:
        bidders = list()
        # scelgo random una localita' da mettere all'asta
        good = goodsRemained[randint(0, len(goodsRemained)-1)]
        # itero sugli offerenti
        for agent in agents:
            if agent.city == good:
                bidders.append((agent, agent.valuation))
        # ordino le offerte in ordine discendente per valutazione
        bidders.sort(key = lambda i:i[1], reverse = True)
        # l'asta non viene aggiudicata a nessuno se non ci sono almeno due offerenti per lo stesso bene
        if len(bidders) > 2:
            auction2[good] = {
                "winner": bidders[0][0],
                "payment": bidders[1][1]
            }
        goodsRemained.remove(good)
print("auction2\n", auction2, "\n\n")
