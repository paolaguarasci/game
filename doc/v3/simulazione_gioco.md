### APPLICHIAMO IL MECCANISMO VCG PER MASSIMIZZARE L'UTILITA' DEI GIOCATORI + VISITARE IL MAGGIOR NUMERO DI CITTA' POSSIBILI

1. Prima di applicare il meccanismo, dobbiamo calcolare le utilità marginali dei giocatori per ogni possibile combinazione di destinazioni (scartiamo a priori quelle che superano i km), che corrisponde alla differenza di costo totale se il giocatore è incluso o escluso dalla combinazione.

Ecco la tabella delle utilità marginali:
__________________________________________________
Giocatore |	Destinazioni	 | Utilità marginale
Alessia	  | Genova	         |  300
Alessia	  | Milano	         |  200
Paola	  | Genova	         |  -50
Paola	  | Milano	         |   50
Sara	  | Genova	         |  100
Sara	  | Milano	         |  200
___________________________________________________

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