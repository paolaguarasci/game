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
