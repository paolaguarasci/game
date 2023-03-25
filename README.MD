# Progetto AGT 2021

https://www.overleaf.com/project/62e6d873cd73a88f96d2ada5

## Traccia

### Scenario:

- Abbiamo un insieme di utenti. Ogni utente propone una lista di coppie (luogo, utilità) corrispondenti all'utilità che ottiene visitando un determinato luogo.
- Non possiamo fidarci dei valori di utilità dichiarati dagli agenti.
- Ogni utente dichiara il pagamento massimo che potrebbe essere disposto a fornire al meccanismo.
- Possiamo fidarci di questa dichiarazione.
- La distanza tra qualsiasi coppia di luoghi è nota, in modo da poter calcolare i percorsi più brevi.
- Ci viene dato un veicolo che può essere prelevato in una data località, che può viaggiare lungo altre località e che alla fine deve tornare al punto di partenza; quindi, il veicolo compie un tour.
- Il veicolo può ospitare un numero fisso, diciamo k, di utenti; inoltre, abbiamo un limite sulla lunghezza massima (espressa in km) del tour.
- L'esecuzione del tour comporta due costi: un costo proporzionale alla lunghezza del tour e un costo fisso.

### Obiettivo:

- Il sistema deve:
  - selezionare l'utente che eseguirà il tour
  - definire i luoghi che saranno visitati dal tour
  - definire i pagamenti che vengono addebitati agli utenti.

### Vincolo:

- A nessun utente può essere addebitato un importo superiore al pagamento massimo che ha dichiarato.

### Desiderata:

- Il costo del tour, che è proporzionale alla lunghezza in km, deve essere equamente distribuito tra gli utenti del veicolo, in modo che nessun agente abbia argomenti per opporsi.
- Il costo fisso deve essere distribuito tra gli agenti in base alle utilità dichiarate, e implementando un meccanismo che porti a dichiarare in modo veritiero le utilità.


- vcg 
- groves 

formalizzare

## Proviamo a buttare giu' qualche idea..

### Setting

- $N = \{1,2,3,...,n\}$ agenti
- la funzione di scelta sociale sceglie il cammino minimo che minimizza la somma dei pesi sugli archi
- Il meccanismo incentiva i player pagandoli (?)

Questo e' un problema utilitario?
Problemi:
- se un agente ha gia' in lista la best choice? Si passa alla seconda?

massimizzare il riempimento della macchina
minimizzare il numero dei km percorsi (quindi la parte variabile del costo)

dati tutti i possibili cammini minimi il meccanismo sceglie:
- il cammino minimo che passa da tutte le citta' del tour

gli agenti mi dichiarano la loro valutazione per la best 

massimizzare il riempimento della macchina
contemporaneamente scegliere il tour piu' breve
vuol dire andare in un posto solo con la macchina piena
massimizzare il riempimento della macchina
contemporaneamente scegliere il tour piu' lungo
vuol dire andare in 5 posti diversi con la macchina piena
chi partecipa al tour?
in totale i posti sono k, come scelgo i k partecipant?
quali citta' scelgo per il tour? 
in totale ci sono 7 citta', posso scegliere n citta' con n in [2,7]

Possiamo vedere la costruzione del tour come un network formation game in cui l'obiettivo del meccanismo e' minimizzare il costo sociale ovvero il costo totale del tour. Se lo vogliamo vedere come un congestion game le risorse limitate sono la macchina, con max k posti, e i km massimi percorribili.


alcune considerazioni teoriche
- ogni global connection game ha un NE
- il prezzo dell'anarchia in un gcg con k player e' al massimo k
- il prezzo della stabilita' in un gcg con k player e' al massimo $H_k$, il k-esimo numero armonico.


# Proviamo a scrivere qualche passaggio
Buonasera Prof, ho studiato il vcg e il groves come mi ha suggerito lei e ho provato ad impostare il problema, in questo modo: 

- k: posti in auto
- maxkm: lunghezza massima del tour
- viaggiatori: potenzialmente infiniti ma almeno 2 (non credo ci sia un lowerbound teorico, penso dipenda da come ho implementato il codice)
- destinazioni possibili: ["rome", "paris", "vienna", "london", "brussels", "berlin", "amsterdam"]
- le utilita' degli egenti sono tutte non negative

Il meccanismo prende in input le valutazioni degli utenti rispetto a tutte le 7 destinazioni e in base a questo compie delle scelte per poter dare in output una lista di partecipanti, una lista di destinazione e i pagamenti per ogni agente partecipante. 

Nel dettaglio le scelte vengono effettuate cosi:

- Scelta delle citta' da visitare
  - ogni player comunica un array di valutazioni, una per ogni citta' sulla mappa
  - le valutazioni si sommano
  - si crea una classifica delle citta' in ordine di decrescente di valutazione
  - partendo dalla prima, tramite tsp di un sottografo, si calcola lo shortest path e si aggiungono citta' fino a raggiungere il kilometraggio massimo consentito

- scelta dei player
  - i player vengono selezionati in base alle loro valutazioni delle citta' che fanno parte del tour, fino ad esaurimento posti

- Pagamento
  - la parte fissa e' costo/occupanti per ogni occupante
  - la parte variabile e' decisa in base alla differenza tra il costo del tour con l'agente e senza l'agente (immaginando che ogni agente venga selezionato per la propria valutazione di una specifica citta')



groves
x(uhat) = prendi la x che massimiza la somma delle valutazini degli agenti


asta combinatoria OR

single-minded bidders 
ogni viaggiatore $i$ piazza un'offerta su una citta' quindi cominica $b_i=(\hat{C_i})$ 


RESERVE PRICE (prezzo di riserva) potrebbe essere il costo minimo del viggio in quel posto li

Buongiorno Prof, 
ho studiato i meccanismi che mi ha suggerito lei, il vcg e il grooves, e anche tutta una serie di altri meccanismi che mi sembrano interessanti dal punto di vista del problema che devo modellare, ovvero le aste in generale e i routing games.

Dopo averci ragionato su vorrei impostare il problema come un'asta combinatoria a piu' elementi dove i beni in vendita sono le tappe del tour (insieme finito). 
L'obiettivo e' massimizzare le citta' visitate, i posti in macchina occupati e al contempo minimizzare il costo totale. L'upper bound delle citta' visitate e' la quantita' totale di citta' nella mappa (7 nei test che sto facendo), l'upper bound dei posti in macchina e' dato dalla traccia ed e' k, il lower bound del costo totale e' 0.
Ogni citta' ha un prezzo di riserva formulato come il costo minimo del passaggio in quella citta'. Se ci sono due o piu' offerte per quella citta' allora il tour passera' da li. Vince il primo offerente ma paga la seconda offerta. (Asta di Vickery)

Qui mi sono bloccata. Nei modelli che ho visto, per problemi simili, gli agenti selezionano un path mentre io vorrei fargli fare le offerte per ogni citta' disponibile una alla volta, con l'idea che questa scelta corrisponda a dire "Sono l'agente 0. Vorrei tanto poter andare a Londra! Offro x per andare a Londra! Se non posso andare a Londra allora vorrei andare a Roma e offro y per andare a Roma" e via dicendo per ogni tappa possibile del tour. Il player quindi fa delle offerte seguendo il suo ordine privato di preferenze ponendole in OR.

Il problema e' il computo del pagamento, in un ottica VCG (con pagamenti di Clarke) ogni utente dovrebbe pagare il costo sociale con la sua scelta meno il costo sociale senza la sua scelta. Per costo sociale intendo il costo del tour (lunghezza in km * costo al km). Ma non ho capito come legare le offerte che i giocatori fanno per la costruzione del tour, con i pagamenti dati dalla selezione dello shortest path e quindi della lunghezza del tour in km che puo' appunto variare in base alle singole decisioni. 

Altra cosa che non mi torna in questo meccanismo che ho disegnato: visto che tutti gli utenti offrono per tutte le citta', se un utente con tipo Roma > Milano > Londra > Berlino viene selezionato per la sua offerta su Roma e il tour poi passa anche da Londra dovrebbe pagare anche per il passagio su Londra visto che ha un utilita' nel passare da Londra e ha fatto un offerta anche su Londra (che non ha vinto)? Mi rendo conto che ragionamento e' un po' ingarbugliato, spero di averlo espresso chiaramente :)

In ogni caso, al di la dei problemi specifici che le ho esposto, vorrei capire se il ragionamento in generale va bene.

