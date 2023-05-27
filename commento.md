# Commento al codice

```python
calculateAllTourWithCost(["milano", "torino", "genova", "roma"])

[(('torino', 'genova', 'roma'), 1342), (('torino', 'roma'), 1340), (('milano', 'torino', 'genova', 'roma'), 1330), (('milano', 'torino', 'roma'), 1159), (('genova', 'roma'), 1000), (('milano', 'genova', 'roma'), 988), (('milano', 'roma'), 692)]

```

Con questa funzione otteniamo tutti i possibili tour a partire da una lista di localita. Si inizia calcolado l'insieme delle parti della lista passata come argomento, a questo insieme di tutti i possibili raggruppamenti di localita' vengono poi sottratti gli insiemi con dimensione minore di 2. Si procede quindi al calcolo delle distanze i km per ognuno dei tour rimasti.

```python
removeTourOverKMLimit(allTour, const.MAXKMFORTOUR)
 [(('milano', 'torino', 'roma'), 1159), (('genova', 'roma'), 1000), (('milano', 'genova', 'roma'), 988), (('milano', 'roma'), 692)]
```

Da qui si ottiene una lista di tour filtrata, ovvero senza i tour che superano il numero massimo di km imposto come vincolo nella traccia.

```python
calculateUtilityForAllTour(tours, agents)
 [(('milano', 'torino', 'roma'), 4), (('milano', 'genova', 'roma'), 4), (('genova', 'roma'), 2), (('milano', 'roma'), 2)]
```

Per ogni tour nell'insieme dei tour passati come parametro, calcola l'utilita' totale sommando le utilita' degli agenti per ognuna delle citta' nel tour in esame.

```python
selectedTour = allTourCappedWithUtility[0]
```

Selezioniamo il tour. Possiamo prendere il primo elemento della lista perche' la funzione di calcolo `calculateUtilityForAllTour` restituisce una lista ordinata per utilita', in ordine inverso. Il primo elemento della lista quindi massimiza l'utilita'.

```python
for agent in agents:
  agent.getCityWithUtility(selectedTour)
```

Qui andiamo ad evidenziare quali sono le citta' di interesse (con utilita' > 0) per ogni agente all'interno del tour selezionato.

```python
calcoloIncassoTotale(selectedTour, agents)
```

Il calcolo dell'incasso totale e' una somma dei singoli pagamenti computati per ogni agente. Qui di seguito la funzione di calcolo di costo per singolo agente.

```python

def calculateAgentPayment(selectedTour, agent):
    agentInterest = agent.getCityWithUtility(selectedTour)
    cityAlternative = []

    for city in selectedTour:
        if city not in agentInterest and city != const.STARTPLACE:
            cityAlternative.append(city)

    agentInterest.append(const.STARTPLACE)
    cityAlternative.append(const.STARTPLACE)
    if len(cityAlternative) > 1 and len(agentInterest) > 1:
        _, costoPercorsoAlternativo = cityNetMoney.findShortestPathBetweenAllSelectedLocations(cityAlternative)
        _, costoTourScelto = cityNetMoney.findShortestPathBetweenAllSelectedLocations(selectedTour)
        _, costoTrattaInteresse = cityNetMoney.findShortestPathBetweenAllSelectedLocations(agentInterest)

        _, distanzaKmTrattaInteresse = cityNetKm.findShortestPathBetweenAllSelectedLocations(agentInterest)
        agent.kmTrattaInteresse = distanzaKmTrattaInteresse

        costo = costoPercorsoAlternativo - (costoTourScelto - costoTrattaInteresse)
        return (costo, agent.budget < costo)
    return (0, True)

```

`cityNetMoney` e `cityNetKm` sono due grafi identici come archi e come nodi, variano solo come pesi sugli archi. Nel primo i pesi rappresentano i `costi in euro`, nel secondo rappresentano i `km`. Su entrambi la funzione `findShortestPathBetweenAllSelectedLocations(lista_localita)` utilizza l'algoritmo TPS per il calcolo dello shortest path tra le localita' passate come argomento.

La funzione di costo quindi calcola:

- `costoPercorsoAlternativo`, costo del percorso alternativo senza l'agente (ovvero il percorso necessario a compiere il tour ma senza la presenza della citta' preferita dall'agente)
- `costoTourScelto`, costo del tour scelto (senza modifiche)
- `costoTrattaInteresse`, costo della tratta di interesse dello specifico agente
  e restituisce in output il costo finale calcolato come `costoPercorsoAlternativo - (costoTourScelto - costoTrattaInteresse)`.

```python
costoRealeTourMoney = getTourCostMoney(selectedTour)
surplus = incassoTotale - costoRealeTourMoney
costoRealeTourKm = getTourCostKm(selectedTour)
costoAlKm = surplus / costoRealeTourKm
```

Qui si calcolano eventuale surplus, il VGC non e' budget balanced!
Il meccanismo potrebbe raccogliere una quantita' di soldi superiore a quella necessaria per fare il viaggio, quindi in `surpluss` appunto.
Il `surplus` abbiamo deciso di utilizzarlo come sconto sulla quota di partecipazione al tour, in misura inversamente proporzionale alla distanza percorsa dai partecipanti al tour per soddisfare la scelta dell'agente di cui si sta calcolando il pagamento.

```python
  for agent in agents:
    print(agent.name)
    calcoloScontoEPagamentoFinale(agent, costoAlKm)
```

Infine la funzione di calcolo dello sconto e del pagamento finale restituire la quota netta da pagare per ogni agente.
