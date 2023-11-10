# Network Security Project: Chosen Ciphertext Attack

Simulation of a simple Chosen Ciphertext Attack in a vulnerable scenario with 'Textbook' RSA cryptography

## Scenario Description
![Sequence Diagram](CCA_sequence_diagram.png)

1. **Bob (Server)**: Holds a secret phrase, and clients must prove they know it. Bob responds with 'ACK' if the received secret phrase is correct; otherwise, he responds with 'NACK' and the decrypted received message.
2. **Alice (Legitimate Client)**: Knows the secret phrase and sends it to the Server.
3. **Eve (Malicious Client)**: Doesn't know the secret phrase but attempts to discover it. Eve intercepts Alice's encrypted message containing the secret phrase and interacts with Bob. She manages to deduce the original message through mathematical operations, exploiting Bob's unsuspecting responses.

## Simulation Instructions
To successfully run the simulation, follow the specified startup order for the components:
1. **Server (Bob)**: Start the server by running `bob.py`.
2. **Legitimate Client (Alice)**: Start the legitimate client by running `alice.py`.
3. **Malicious Client (Eve)**: Start the malicious client by running `eve.py`.

## Requirements
To execute the simulation successfully, ensure you have the following Python libraries installed:
- [Flask](https://pypi.org/project/Flask/)
- [Cryptography](https://pypi.org/project/cryptography/)
- [Requests](https://pypi.org/project/requests/)
- [Libnum](https://pypi.org/project/libnum/)
