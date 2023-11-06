# NetworkSecurity

## Descrizione Scenario
1. **Bob (Server)**: Conserva una frase segreta e i client devono dimostrare di conoscerla. Bob risponde con 'ACK' se la frase segreta ricevuta è corretta, altrimenti, risponde con 'NACK' e il messaggio ricevuto decifrato.
2. **Alice (Client legittimo)**: Conosce la frase segreta e la invia al Server.
3. **Eve (Client malizioso)**: Non conosce la frase segreta ma tenta di individuarla. Intercetta il messaggio cifrato di Alice che contiene la frase segreta e interagisce con Bob. Riesce a risale al messaggio originario mediante operazioni matematiche, sfruttando le risposte incaute di Bob.

## Istruzioni per la Simulazione
Per eseguire la simulazione, seguire il seguente ordine di avvio dei componenti:
1. **Server (Bob)**: Avviare il server eseguendo `bob.py`.
2. **Client legittimo (Alice)**: Avviare il client legittimo eseguendo `alice.py`. 
3. **Client malizioso (Eve)**: Avviare il client malizioso eseguendo `eve.py`.
