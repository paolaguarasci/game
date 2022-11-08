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
