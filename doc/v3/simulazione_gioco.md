Posti k = 3
Partenza Roma
Città = [Roma,Genova,Milano]
Players = [Alessia=1,Paola=2,Sara=3]
Assi = [
    'Roma-Genova'='1',
    'Roma-Milano'='2',
    'Roma-Genova-Milano'='3'
]
Preferenze = {
    Alessia = [0,5,4]
    Paola   = [0,4,2]
    Sara    = [0,1,2]
}


roma-genova         alessia  senza 5 - con 10   = -5
roma-milano         alessia  senza 4 - con 8    = -4
roma-genova-milano  alessia  senza 9 - con 18   = -9

### APPLICHIAMO IL MECCANISMO VCG PER MASSIMIZZARE L'UTILITA' DEI GIOCATORI + VISITARE IL MAGGIOR NUMERO DI CITTA' POSSIBILI

1. Prima di applicare il meccanismo, dobbiamo calcolare le utilità marginali dei giocatori per ogni possibile combinazione di destinazioni (scartiamo a priori quelle che superano i km), che corrisponde alla differenza di costo totale se il giocatore è incluso o escluso dalla combinazione.

Ecco la tabella delle utilità marginali:
__________________________________________________
Giocatore |	Destinazioni	   | Utilità marginale

Alessia	  | Roma-Genova        |  5 - 4     =  1
Alessia	  | Roma-Milano        |  4 - 5     = -1 
Alessia	  | Roma-Genova-Milano |  5 - 4 - 4 = -3

Paola	  | Roma-Genova  	   |  4 - 2     = 2
Paola	  | Roma-Milano	       |  2 - 2     = 0
Paola	  | Roma-Genova-Milano |  4 - 2 - 2 = 0

Sara	  | Roma-Genova  	   |    3
Sara	  | Roma-Milano	       |    2
Sara	  | Roma-Genova-Milano |    3
___________________________________________________

Per calcolare l'utilità marginale di ogni giocatore per ogni combinazione di destinazioni, ho utilizzato la seguente formula (secondo VCG):

Utilità marginale = Utilità totale della combinazione senza il giocatore - Utilità totale della combinazione con il giocatore

E' stata calcolata l'utilità totale di una combinazione di destinazioni escludendo il giocatore in questione, e poi si è sottratto l'utilità totale della stessa combinazione con il giocatore incluso, ottendo così l'utilità marginale del giocatore per quella particolare combinazione.

#### Calcolo utilità marginale di Alessia per la combinazione "Roma-Genova-Milano"

Utilità marginale di Alessia per "Roma-Genova-Milano" = Utilità totale di "Roma-Genova-Milano" senza Alessia - Utilità totale di "Roma-Genova-Milano" con Alessia

Utilità marginale di Alessia per "Roma-Genova-Milano" = 9 - 1 = 4

In base a queste utilità marginali, possiamo calcolare il pagamento di ciascun giocatore per ogni possibile combinazione di destinazioni. Il pagamento corrisponde alla somma delle utilità marginali degli altri giocatori se il giocatore è incluso nella combinazione, meno la somma delle utilità marginali degli altri giocatori se il giocatore è escluso dalla combinazione.

Tabella dei pagamenti:

Giocatore |	Destinazioni	 |  Pagamento
Alessia	  | Genova	         |   50
Alessia	  | Milano	         |    0
Paola	  | Genova	         |    0
Paola	  | Milano	         |   50
Sara	  | Genova	         |  150
Sara	  | Milano	         |    0
___________________________________________________

In base a questi pagamenti, possiamo determinare la combinazione di destinazioni che massimizza le utilità totali dei giocatori, tenendo conto dei loro budget. Possiamo farlo in modo iterativo, partendo dalla combinazione di destinazioni che include tutte e tre le città e rimuovendo una città alla volta finché non si raggiunge una combinazione che soddisfa i budget dei giocatori.

Ecco la sequenza di combinazioni:

Destinazioni	    |Costo totale	|Utilità totale	| Alessia paga	| Paola paga |	Sara paga
Roma-Genova-Milano	| 300	        |18 	        | 150	        |   50	     |     150
Roma-Genova	        | 200	        |10 	        | 50	        |    0	     |     150
Roma-Milano	        | 150	        |8  	        | 0             |   50	     |       0
Roma	            |   0           |0	            | 0	            |    0       |       0


La combinazione di destinazioni che massimizza le utilità totali dei giocatori è "Roma-Genova-Milano", con un costo totale di 300 euro e un'utilità totale di 18. 
In questa combinazione, Alessia paga 150 euro, Paola paga 50 euro e Sara paga 150 euro.

La combinazione "Roma-Genova" è la seconda migliore, con un costo totale di 200 euro e un'utilità totale di 10. In questa combinazione, Alessia paga 50 euro e Sara paga 150 euro, ma Paola non può partecipare a causa del suo budget limitato.

La terza migliore combinazione è "Roma-Milano", con un costo totale di 150 euro e un'utilità totale di 8. In questa combinazione, Alessia non partecipa, Paola paga 50 euro e Sara non partecipa.

In conclusione, il tour finale consiste nella combinazione di destinazioni "Roma-Genova-Milano", che massimizza le utilità totali dei giocatori, tenendo conto dei loro budget. Alessia paga 150 euro, Paola paga 50 euro e Sara paga 150 euro. La combinazione "Roma-Genova" sarebbe stata la seconda migliore, ma Paola non può partecipare a causa del suo budget limitato.

----------------------
In pratica, si può utilizzare il valore di Shapley per calcolare la contribuzione individuale di ogni partecipante e utilizzare questi valori come base per la determinazione dei costi nel meccanismo di VCG. In questo modo, si può tenere conto della contribuzione di ciascun partecipante al risultato finale e assicurarsi che il meccanismo di assegnazione finale sia equo e incentivi il comportamento cooperativo tra i partecipanti.
------------------------


Sto organizzando un tour in autobus con 2 posti. 
La partenza è da Roma. 
Le destinazioni sono Roma, Genova, Milano. 
Ho tre giocatori. 
Alessia vuole andare a Genova con preferenza 5 o a Milano con preferenza 4. 
Paola vuole andare a Milano con preferenza 2 o a Genova con preferenza 4. 
Sara vuole andare a Genova con preferenza 1 o a Milano con preferenza 2. 
L'asse Roma-Milano costa 150 euro, l'asse Roma-Genova costa 200 euro, l'asse Milano-Genova costa 100 euro, l'asse Roma-Genova-Milano costa 300 euro. 
Paola ha un budget di 300 euro. Alessia ha un budget di 500 euro.
Sara ha un budget di 400 euro. 
Puoi applicare il VCG massimizzando le utilità e visitando più città possibili? Quale sarebbe il tour finale? Chi partecipa non può pagare 0 euro.
Chi partecipa al tour?




Scenario:
- We are given a set of users. Each user proposes a list of pairs (location, utility) corresponding to the utility s/he gains for visiting a given location; we cannot trust on the utility values declared by the agents; Moreover, each user declares the maximum payment s/he might be willing to provide to the mechanism; we can trust this declaration.
- The distance between any pairs of locations is known, so that we can compute shortest paths.
- We are given a vehicle that can be picked in a given location, that can travel along other locations
and that eventually must return to the starting point; hence, the vehicle performs a tour.
- The vehicle can accommodate a fixed number, say k, of users; moreover, we have a bound on the
maximum length (expressed in km) of the tour.
- Performing the tour gives rise to two costs: a cost proportional to the length of the tour and a fixed
cost.

Goal:
- The system has to select the user that will perform the tour; it has to define the locations that will
be visited by the tour; and it has to define the payments that are charged to the users.

Constraint:
- No user can be charged more that the maximum payment s/he has declared.

Desiderata:
- The cost of the tour which is proportional to the length in km has to be fairly distributed among the users on the vehicle, in a way that no agent has arguments to object.
- The fixed cost has to be distributed among the agents based on the declared utilities, and by implementing a mechanisms that lead to truthfully declare the utilities.



----


Yes, we can apply the Vickrey-Clarke-Groves (VCG) mechanism to determine the optimal tour for the three participants while maximizing their utility. The VCG mechanism is a way of designing a truthful and efficient auction that ensures that the participants' incentives are aligned with the social welfare objectives.

To apply the VCG mechanism, we need to first calculate the utility of each participant for each possible tour. The utility is calculated as the difference between the participant's maximum willingness to pay for a particular tour and the actual price paid by the participant.

For example, if Alessia's maximum willingness to pay for the Rome-Genoa-Milan tour is 500 euros, and the actual price paid by Alessia is 300 euros, then Alessia's utility for that tour is 200 euros (i.e., 500 - 300).

Next, we need to find the socially optimal tour, which maximizes the sum of the utilities of all participants. One way to do this is to use integer programming to find the tour that maximizes the sum of the utilities subject to the constraints that each city is visited at most once and the total cost of the tour is within the budgets of all participants.

Using this approach, we can find that the socially optimal tour is to travel from Rome to Genoa to Milan, which costs 300 euros. This tour maximizes the total utility of all participants, which is 11 (i.e., 5 + 2 + 4).

Now we need to determine the payments that each participant should make. For this, we need to calculate the externalities that each participant imposes on the others by participating in the tour. The externalities are calculated as the difference in the total utility of all participants with and without the participant's participation.

For example, if Alessia does not participate in the tour, then the total utility of Paola and Sara would be 6 (i.e., 2 + 4), but if Alessia participates in the tour, then the total utility of all participants is 11 (i.e., 5 + 2 + 4). Therefore, the externality imposed by Alessia is 5 (i.e., 11 - 6).

Using the externality values, we can calculate the payments that each participant should make using the VCG mechanism. The payment of each participant is equal to the sum of the externalities imposed on the other participants by the participant's participation in the tour.

Thus, the payment that Alessia should make is 6 (i.e., 5 + 1), the payment that Paola should make is 5 (i.e., 2 + 3), and the payment that Sara should make is 0 (i.e., 1 + 2 - 3).

Therefore, the final tour would be from Rome to Genoa to Milan, and the payments of each participant would be Alessia: 6 euros, Paola: 5 euros, Sara: 0 euros.

----

!

Yes, we can apply the Vickrey-Clarke-Groves (VCG) mechanism to maximize the utility of the participants and visit as many cities as possible.

First, let's calculate the total cost of each possible tour:

    Rome-Milan: 150 euros
    Rome-Genoa: 200 euros
    Milan-Genoa: 100 euros
    Rome-Genoa-Milan: 300 euros

Next, let's calculate the utility for each participant on each possible tour:

    Paola:
        Rome-Milan: 2
        Rome-Genoa: 4
        Milan-Genoa: 0
        Rome-Genoa-Milan: 0
    Alessia:
        Rome-Milan: 4
        Rome-Genoa: 5
        Milan-Genoa: 0
        Rome-Genoa-Milan: 9
    Sara:
        Rome-Milan: 2
        Rome-Genoa: 1
        Milan-Genoa: 2
        Rome-Genoa-Milan: 3

Now, let's calculate the total utility of each possible tour:

    Rome-Milan: 8 (4+2+2)
    Rome-Genoa: 10 (5+4+1)
    Milan-Genoa: 2 (0+0+2)
    Rome-Genoa-Milan: 12 (9+3+0)

We can see that the Rome-Genoa-Milan tour has the highest total utility. However, it exceeds the budget of Paola, who can only afford a tour costing up to 300 euros.

To find the optimal tour, we need to consider all possible subsets of the cities and choose the one with the highest total utility that fits within the budget constraints of all participants.

Here are the possible subsets of cities and their total


---

I am organising a tour for 2 people. Departure is from Rome. The destinations are Genoa, Milan, Torino. I have 3 people. 

Alessia's preferences are [0,1,4,5]
Paola's preferences are [0,5,3,0]
Sara's preferences are [0,2,5,0]

The Rome-Milan route costs 150 euros, the Rome-Genoa route costs 200 euros, the Roma-Torino route costs 400 euros, the Rome-Genoa-Milan route costs 300 euros, the Rome-Genoa-Milan-Torino route costs 600 euros. Paola has a budget of 300 euros, Alessia 500 euros, Sara 400 euros. Can you apply the VCG by maximising utility and visiting as many cities as possible? Those who participate cannot pay 0 euro. If a player does not participate in the tour he pays 0 euros.


---

Si può utilizzare l'algoritmo VCG per massimizzare le utilità e determinare il tour finale.
Prima di tutto, si determina il costo marginale di ciascun giocatore per ogni asse, ovvero il costo totale del viaggio senza di loro meno il costo totale del viaggio con loro. Ad esempio, il costo marginale di Alessia per l'asse Roma-Milano è 150 euro, mentre il suo costo marginale per l'asse Roma-Genova è 50 euro (200-150). I costi marginali per ciascun giocatore e per ciascun asse sono riportati nella tabella sottostante:

 
Roma-Milano
Roma-Genova
Milano-Genova
Roma-Genova-Milano


Alessia
150
50
100
300

Paola
0
50
0
150

Sara
50
0
100
200

Successivamente, si calcola l'utilità totale che ciascun giocatore apporterebbe al tour, scegliendo la sua destinazione preferita. Ad esempio, se Alessia va a Genova, la sua utilità sarebbe 5. Se invece va a Milano, la sua utilità sarebbe 4. Questi calcoli sono riportati nella seguente tabella:

 
Roma-Milano
Roma-Genova
Milano-Genova
Roma-Genova-Milano


Alessia
4
5
4
0

Paola
2
4
2
0

Sara
2
1
2
0

Si utilizza l'algoritmo VCG per determinare la combinazione di destinazioni che massimizza l'utilità totale, tenendo conto dei costi marginali di ciascun giocatore. In pratica, si considerano tutte le possibili combinazioni di destinazioni e si sceglie quella che massimizza la somma delle utilità dei giocatori meno i costi marginali degli altri giocatori.
La combinazione di destinazioni che massimizza la somma delle utilità meno i costi marginali è quella in cui Alessia va a Genova, Paola va a Milano e Sara non partecipa al tour. In questo caso, l'utilità totale sarebbe 9, che corrisponde alla somma delle utilità di Alessia e Paola meno il costo marginale di Sara per l'asse Roma-Milano.
Il costo totale del tour sarebbe di 250 euro, che è inferiore al budget di ogni giocatore. Il tour finale sarebbe quindi il seguente: Roma -> Genova -> Milano -> Roma.
