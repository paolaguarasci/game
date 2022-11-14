# Progetto AGT 2021

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
- Scelta delle citta' da visitare
  - ogni player comunica un array di valutazioni, una per ogni citta' sulla mappa
  - le valutazioni si sommano
  - si crea una classifica delle citta' piu' valutate
  - partendo dalla prima, tramite tsp, si calcola lo shortest path e si aggiungono citta' fino a raggiungere il kilometraggio massimo consentito
- scelta dei player
  - i player vengono selezionati in base alle loro valutazioni delle citta' che fanno parte del tour
- Pagamento
  - Tramite VCG 