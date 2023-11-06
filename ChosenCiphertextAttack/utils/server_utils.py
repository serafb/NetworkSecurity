from utils.path_url import *
from utils.rsa_tools import *
import json

def define_encrypt_secret(bob_e,bob_N):
#Definisce una nuova frase segreta, la cifra con textbook RSA (no padding) usando la Public Key di Bob
    frase_segreta  = "SSC Napoli CAMPIONE DI ITALIA 2023"
    int_frase_segreta = testo_a_intero(frase_segreta)
    encrypted_frase_segreta = cifratura_textbook(int_frase_segreta, bob_e, bob_N)
    return encrypted_frase_segreta

def generate_store_bob_keys(size = 2048, public_exponent=65537): #public_e = 65537 ,public_e =  3
#Genera e Scrive su file PublicKey, PrivateKey
    #Genera Public e Private key
    bob_private_key, bob_public_key = generate_key_pair(size, public_exponent)
    bob_e,bob_N  = publickey_parameters(bob_public_key)
    bob_d,bob_N1 = privatekey_parameters(bob_private_key)
    assert bob_N == bob_N1, "Errore estrazione (e,N) (d,N): N diversa!"
    #Scrive su file Public e Private key
    public_data = [ { "e": bob_e, "N": bob_N } ]
    with open(PATH_bob_publickey, 'w') as json_file:
        json.dump(public_data, json_file)
    private_data = [ { "d": bob_d, "N": bob_N } ]
    with open(PATH_bob_privatekey, 'w') as json_file:
        json.dump(private_data, json_file)
    return bob_e,bob_N,bob_d

def load_bob_publickey():
#Carica da file
    with open(PATH_bob_publickey, 'r') as json_file:
        loaded_data = json.load(json_file)
    bob_e = int(loaded_data[0]['e'])
    bob_N = int(loaded_data[0]['N'])
    return bob_e,bob_N

def load_bob_privatekey():
    with open(PATH_bob_privatekey, 'r') as json_file:
        loaded_data = json.load(json_file)
    bob_d = int(loaded_data[0]['d'])
    bob_N = int(loaded_data[0]['N'])
    return bob_d,bob_N