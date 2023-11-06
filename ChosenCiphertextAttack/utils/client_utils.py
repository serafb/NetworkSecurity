from utils.path_url     import *
from utils.rsa_tools    import *
import requests

#Get
def get_bob_publickey():
    response = requests.get(URL_server_publickey)
    if response.status_code == 200:
        data = response.json()
        bob_e = data['e']
        bob_N = data['N']
    else:
        print('Errore nella richiesta al server.')
    return bob_e,bob_N

#Post
def send_parola_segreta(frase_to_send,e_val,N_val):
    my_secret_encrypted  = encrypt_textbookRSA(frase_to_send,e_val,N_val)
    # POST encrypted secret
    store_message_alice_to_bob(my_secret_encrypted)     # Memorizza su file
    resp_from_bob = send_to_bob(my_secret_encrypted)    # Effettua Post
    check_bob_res(resp_from_bob)                        # Legge e verifica risposta
    return resp_from_bob

def send_to_bob(my_secret_encrypted):
    #INVIO msg a Server
    payload = {'message': int(my_secret_encrypted)}                      # Creazione messaggio da inviare a Bob
    response = requests.post(URL_server_message, json=payload)   
    #RICEZIONE msg da Server
    if response.status_code == 200:                                         # Controlla se la richiesta ha avuto successo (codice di stato 200)
        data_from_bob = response.json()                                     # Ricevi il valore come JSON e memorizzalo in una variabile                                        
        return data_from_bob
    else:
        print("Errore nella richiesta al server Bob:", response.status_code)
        return ""

# Verifica risposta di Bob
def check_bob_res(resp_from_bob):
    if resp_from_bob == "ACK":
        print(f"[ BOB ]:\t FRASE SEGRETA CORRETTA. -  Il Server ha risposto: \t{resp_from_bob}")
        return True
    else:
        formatted_resp_from_bob = "{:.30s}".format(str(resp_from_bob))
        print(f"[ BOB ]:\t FRASE SEGRETA ERRATA!   -  Il Server ha decifrato: \t{formatted_resp_from_bob}... (continua)")
        return False


# Memorizza e Carica messaggi su/da file
def store_message_alice_to_bob(message):
    with open(PATH_communications_a_b, 'w') as file:
        file.write(str(message))

def load_message_alice_to_bob():
    with open(PATH_communications_a_b, 'r') as file:
        stored = int(file.read())
    return stored