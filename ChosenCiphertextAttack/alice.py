from utils.path_url     import *
from utils.client_utils import *

print("\n* * * * * CLIENT STARTED * * * * *")
input("\n\t\t Premi Invio per chiedere a Bob la PublicKey.")

# GET Bob Public Key
bob_e,bob_N = get_bob_publickey()
print(f"[ALICE]:\t Ho ricevuto la Public Key del server Bob")

# -> INVIO n.1 (caso errato)
input("\n\t\t Premi Invio per provare la prima Frase Segreta.")
print("\n[ALICE]:\t *** Invio ***  Tentativo n.1")
parola_segreta_to_send = "GASPERINI Allenatore"
print(f"[ALICE]:\t Cifro e Invio la mia Frase Segreta a Bob:\t{parola_segreta_to_send}")
send_parola_segreta(parola_segreta_to_send,bob_e,bob_N)

# -> INVIO n.2 (caso corretto)
input("\n\t\t Premi Invio per provare la seconda Frase Segreta.")
print("\n[ALICE]:\t *** Invio ***  Tentativo n.2")
parola_segreta_to_send = "SSC Napoli CAMPIONE DI ITALIA 2023"
print(f"[ALICE]:\t Cifro e Invio la mia Frase Segreta a Bob:\t{parola_segreta_to_send}")
send_parola_segreta(parola_segreta_to_send,bob_e,bob_N)

print("* * * * * CLIENT ENDED * * * * *\n")
input("Premi Invio per uscire...")