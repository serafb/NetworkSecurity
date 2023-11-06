from utils.path_url     import *
from utils.client_utils import *
from utils.rsa_tools    import *
import random
import libnum

print("\n* * * * * EVE STARTED * * * * *")
input("\n\t\t Premi Invio per chiedere a Bob la PublicKey.")

# GET Bob Public Key
bob_e,bob_N = get_bob_publickey()
print(f"[ EVE ]:\t Ho ricevuto la Public Key del server Bob")

input("\n\t\t Premi Invio per caricare il messaggio cifrato C (intercettato tra Alice e Bob).")
#LOAD Messaggio (Chiave Segreta) cifrato inviato da Alice a Bob 
intercepted_message = load_message_alice_to_bob()
formatted_intercepted_message = "{:.30s}".format(str(intercepted_message))
print(f"\n[ EVE ]:\t Ho intercettato la seguente comunicazione cifrata tra Alice e Bob:\n\t\t C = {formatted_intercepted_message}... (continua)")

input("\n\t\t Premi Invio per calcolare il nuovo messaggio cifrato C'")
#CALCOLO di un nuovo messaggio: (MSG_cifrato_intercettato x RAND^e)mod_N
print("[ EVE ]:\t Calcolo un nuovo messaggio come segue: C' = (C x R^e)mod_N")
rand_value = random.randint(2, 99)
tampered_message_from_alice = (intercepted_message * pow(rand_value,bob_e,bob_N) ) % bob_N
formatted_tamp_msg = "{:.30s}".format(str(tampered_message_from_alice))
print(f"[ EVE ]:\t Il nuovo messaggio 'esca' calcolato è il seguente:\n\t\t C' = {formatted_tamp_msg}... (continua)")

#POST n.1
input("\n\t\t Premi Invio per inviare al server C'")
print(f"\n[ EVE ]:\t Invio il messaggio calcolato (non corrisponde sicuramente alla Frase Segreta)")
resp_from_bob = send_to_bob(tampered_message_from_alice)
check_from_bob = check_bob_res(resp_from_bob)

#Calcolare inverso modulare
input("\n\t\t Premi Invio per risalire matematicamente alla Frase Segreta")
print(f"\n[ EVE ]:\t Utilizzo la risposta M' di Bob per calcolare la Frase Segreta calcolando M' x R^-1 mod_N")
inv_resp_from_bob =  (resp_from_bob * libnum.invmod(rand_value,bob_N)) % bob_N
maybe_the_secret = intero_a_testo(inv_resp_from_bob)
print(f"[ EVE ]:\t Credo che la frase segreta sia:\t M* = {maybe_the_secret}\n\t\t Invio a Bob per la verifica ...\n")

#Cifro con chiave di BOB
encr_inv_resp_from_bob = cifratura_textbook(inv_resp_from_bob,bob_e,bob_N)

#POST n.2
resp_from_bob = send_to_bob(encr_inv_resp_from_bob)
check_from_bob = check_bob_res(resp_from_bob)
if check_from_bob == True:
    print(f"\n[ EVE ]:\t Sono riuscito a risalire alla FRASE SEGRETA!!!!\n\t\t M = {maybe_the_secret}")
else:
    print(f"\n[ EVE ]:\t Non sono stato in grado di risalire alla FRASE SEGRETA")

print("* * * * * EVE ENDED * * * * *\n")
input("Premi Invio per uscire...")