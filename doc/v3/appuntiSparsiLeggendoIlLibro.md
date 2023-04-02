La teoria *social choice* e' non-strategica. Prende le preferenze degli agenti per come sono, ed investiga i modi i cui possono essere aggregate. Ma spesso queste preferenze non sono note, quelle che sono note sono le *dichiarazioni* di preferenze, che possono essere veritiere o no. 

Supponiamo di avere agenti self-interested, in generale non rivelano le loro vere preferenze. Poiché il progettista desidera trovare un risultato ottimale rispetto alle vere preferenze degli agenti (ad esempio, eleggere un leader che rifletta davvero le preferenze degli agenti), l'ottimizzazione rispetto alle preferenze dichiarate **non** raggiungerà in generale l'obiettivo.

Il design dei meccanismi e' una versione strategica della social choice theory, in cui si da per scontato che gli agenti siano interessati a massimizzare il loro payoff. 

È qui che entra in gioco la progettazione dei meccanismi, o teoria dell'implementazione. Nella teoria dell'implementazione dei meccanismi, la progettazione dei meccanismi viene talvolta chiamata in modo colloquiale teoria dei giochi inversa. La nostra discussione sulla teoria dei giochi nel Capitolo 3 è stata impostata come segue: Data un'interazione tra un insieme di agenti, come possiamo prevedere o prescrivere il corso d'azione dei vari agenti che partecipano all'interazione? Nella progettazione di meccanismi, piuttosto che studiare una determinata interazione strategica, si parte da alcuni comportamenti desiderati da parte degli agenti e ci si chiede quale interazione strategica tra questi agenti potrebbe dare origine a tali comportamenti. In linea di massima, dal punto di vista tecnico, ciò si traduce in quanto segue. Assumeremo preferenze individuali sconosciute e ci chiederemo se possiamo progettare un gioco tale che, indipendentemente dalle preferenze segrete degli agenti, l'equilibrio del gioco sia garantito da una certa proprietà o da un insieme di proprietà desiderate. La progettazione di meccanismi è forse la parte più "informatica" della teoria dei giochi, poiché si occupa di progettare protocolli efficaci per sistemi distribuiti. La differenza fondamentale rispetto al lavoro tradizionale sui sistemi distribuiti è che nel contesto attuale gli elementi distribuiti non sono necessariamente cooperativi e devono essere motivati a fare la loro parte. Per questo motivo si può pensare alla progettazione di meccanismi come a un esercizio di "ingegneria degli incentivi".

### Differenza tra un gioco beyasiano classico e un gioco beyasiano in design dei meccanismi. 
Iniziamo introducendo alcuni principi generali di progettazione dei meccanismi, senza porre alcuna restrizione alle preferenze che gli agenti possono avere. Poiché la progettazione di meccanismi è più spesso studiata in contesti in cui le preferenze degli agenti sono sconosciute, iniziamo definendo un contesto di gioco bayesiano, basandoci sulla definizione di tipi epistemici di giochi bayesiani data nella Sezione 6.3.1. La differenza fondamentale è che il contesto non include azioni per gli agenti e definisce invece le funzioni di utilità sull'insieme dei possibili agenti. La differenza fondamentale è che l'impostazione non include le azioni degli agenti e definisce invece le funzioni di utilità sull'insieme dei possibili risultati.

### Gioco Bayesiano 
E' una tupla con (N, O, Theta, p, u) dove:
- N set finito di n agenti 
- O set finito (?) dei possibili outcome
- Theta (prodotto cartesiano tra i Theta degli agenti, uno per ogni agente) is a set of possible joint type vectors
- p distribuzione di probabilita' di Theta
- u insieme delle funzioni di utilita' degli agenti

### Meccanismo 
Un meccanismo per un gioco bayesiano e' una coppia (A,M) dove:
- A=A1x...xAn insieme di azioni disponibili per ogni agente i-esimo
- M mappa ogni action profile su una distribuzione degli outcome (???)
Un meccanismo e' **deterministico** se per ogni azione in A esiste un outcome in O tale che M(a)(o) = 1, cioe' ogni azione in a porta ad un outcome prestabilito. In questo caso possiamo scrivere semplicemente M(a) = o, senza tenere conto delle propabilita'.

### Implementazione in strategia dominante

Dato un setting di gioco bayesiano, un meccanismo e' implementato in strategia dominante per una funzione di scelta sociale C (su N agenti e O outcomes) se per ogni vettore delle utilita' u, il gioco ha un equilibrio in strategia dominante, e in ogniuno di questi equilibri a* abbiamo M(a*)=C(u).

Il lettore attento noterà che, poiché abbiamo definito in precedenza le funzioni di scelta sociale come deterministiche, ci ritroviamo con un meccanismo che seleziona anche gli esiti in modo deterministico. Naturalmente, questa definizione può essere estesa per descrivere funzioni di scelta sociale e meccanismi randomizzati.
Un meccanismo che dà luogo a strategie dominanti viene talvolta definito a prova di strategia, perché non è necessario che gli agenti ragionino sulle azioni degli altri per massimizzare la loro utilità.

Nell'esempio della babysitter, le frasi "ogni bambino vota per una scelta" e "l'attività selezionata è quella con il maggior numero di voti, eliminando i pareggi in ordine alfabetico" sono un meccanismo ben formato, poiché specifica le azioni a disposizione di ogni bambino e l'esito a seconda delle scelte fatte. 
Si consideri ora la funzione di scelta sociale "l'attività selezionata è quella che è la prima scelta del numero massimo di bambini, rompendo i legami in ordine alfabetico". È chiaro che il meccanismo definito dalla babysitter non implementa questa funzione in strategie dominanti. Per esempio, l'istanza precedente non ha una strategia dominante per Ray (il ragazzino che voleva imbrogliare).

### Implementation in Bayes–Nash equilibrium

Dato un setting di gioco bayesiano, un meccanismo e' implementato in BayesNash eq per una funzione di scelta sociale C (su N agenti e O outcomes) se esiste un equilibrio di nash per il gioco ad informazione incompleta tale che per ogni tipo theta e per ogni profilo di azione a che puo' esistere a partire da theta, abbiamo M(a) = C(u(., Theta))

Un esempio classico di progettazione di meccanismi bayesiani è la progettazione di aste. Il progettista desidera, ad esempio, garantire che l'offerente con la valutazione più alta per un determinato oggetto vinca l'asta, ma le valutazioni degli agenti sono tutte private. I risultati consistono nell'assegnare l'oggetto (nel caso di un'asta semplice, a singolo oggetto) a uno degli agenti e nel far sì che gli agenti effettuino o ricevano dei pagamenti. Le regole dell'asta definiscono le azioni disponibili per gli agenti (le "regole di offerta") e la mappatura dai vettori di azione ai risultati ("regole di allocazione" e "regole di pagamento": chi vince e chi paga cosa in funzione dell'offerta). Se assumiamo che le valutazioni siano estratte da una distribuzione nota, ogni particolare disegno d'asta e ogni particolare insieme di agenti definisce un gioco bayesiano, in cui il segnale di ciascun agente è la propria valutazione.

Infine, esistono concetti di implementazione che sono soddisfatti da un insieme più ampio di profili strategici rispetto all'implementazione in strategie dominanti, ma che non sono garantiti come realizzabili per qualsiasi funzione di scelta sociale e insieme di preferenze, a differenza dell'implementazione di Bayes-Nash. Ad esempio, potremmo considerare solo equilibri simmetrici di Bayes-Nash, in base al principio che le strategie che dipendono dall'identità dell'agente, è meno probabile che si verifichino nella pratica. Si scopre che gli equilibri simmetrici di Bayes-Nash esistono sempre nei giochi simmetrici bayesiani. Una seconda nozione di implementazione che merita di essere menzionata è l'implementazione ex post. Ricordiamo dalla Sezione 6.3.4 che un equilibrio ex post ha la proprietà che nessun agente può mai guadagnare cambiando la propria strategia anche se osserva i tipi degli altri agenti, finché tutti gli altri agenti seguono le strategie dell'equilibrio. Quindi, a differenza di un equilibrio di Bayes-Nash, un equilibrio ex post non dipende dalla distribuzione dei tipi. Indipendentemente dal concetto di implementazione, si può richiedere che la funzione di scelta sociale desiderata sia implementata nell'unico equilibrio, in ogni equilibrio o in almeno un equilibrio del gioco sottostante.

### Principio di rivelazione

Una proprietà che spesso si desidera ottenere dai meccanismi è la veridicità.
Questa proprietà è valida quando gli agenti rivelano sinceramente le loro preferenze al meccanismo in equilibrio. 
**Si scopre che questa proprietà può essere sempre raggiunta indipendentemente dalla funzione di scelta sociale implementata e dalle preferenze degli agenti.** 
Più formalmente, un meccanismo **diretto** è un meccanismo in cui **l'unica azione disponibile** per ogni agente è l'annuncio diretto delle proprie informazioni private. Poiché in un gioco bayesiano l'informazione privata di un agente è il suo tipo, i meccanismi diretti hanno Ai = Θi. Quando l'insieme di azioni di un agente è l'insieme di tutti i suoi possibili tipi, egli può mentire e annunciare un tipo qualunque diverso dal suo vero tipo. Un meccanismo diretto si dice veritiero (o compatibile con gli incentivi) se, per qualsiasi vettore di tipi θ, nell'equilibrio del gioco definito dal meccanismo la strategia di ogni agente i è quella di annunciare il suo vero tipo. Possiamo quindi parlare di compatibilità degli incentivi nelle strategie dominanti e compatibilità degli incentivi di Bayes-Nash. La nostra affermazione secondo cui la veridicità può sempre essere la compatibilità di incentivo di Bayes-Nash implica, ad esempio, che le funzioni di scelta sociale implementabili da meccanismi veritieri a strategia dominante sono esattamente quelle implementabili da meccanismi diretti a prova di strategia. Questo significa che possiamo, senza perdere la copertura, limitarci a una piccola porzione dello spazio di tutti i meccanismi

**Teorema 10.2.5 (principio di rivelazione)** Se esiste un qualsiasi meccanismo che implementa una funzione di scelta sociale C in strategie dominanti, allora esiste un meccanismo diretto che implementa C in strategie dominanti ed è veritiero.

