#SERVER
from utils.server_utils import *
from flask import Flask, send_file, request, jsonify

print("\n* * * * * SERVER STARTING * * * * *\n[ BOB ]:\t INIZIALIZZAZIONE ...")
#Genera PublicKey, PrivateKey
# ->decommenta per generare nuove chiavi
print(f"[ BOB ]:\t Genero la mia Public Key e la mia Private Key")
bob_e,bob_N,bob_d = generate_store_bob_keys(size = 2048, public_exponent=65537) # ->commenta per usare chiavi già generate

#LOAD Public Key Private Key
bob_e,bob_N = load_bob_publickey()
bob_d,bob_N = load_bob_privatekey()
print(f"[ BOB ]:\t Ho caricato la mia Public Key e la mia Private Key")

#Definizione e cifratura Frase Segreta
print(f"[ BOB ]:\t Definisco e cifro la Frase Segreta")
encrypted_frase_segreta = define_encrypt_secret(bob_e,bob_N)

print(f"[ BOB ]:\t Starting service...")

app = Flask(__name__)

# Endpoint per restituire una pagina HTML
@app.route('/')
def index():
    return send_file('utils/index.html')

# Endpoint per restituire la Public Key di Bob tramite il metodo GET
@app.route('/get_publickey', methods=['GET'])
def get_publickey():
    data = {'e': bob_e, 'N': bob_N}
    return jsonify(data)

# Endpoint per ricevere messaggi tramite il metodo POST
@app.route('/post_message', methods=['POST'])
def post_data():
    data = request.json
    encrypted = int(data['message'])
    if encrypted == encrypted_frase_segreta:
        response = "ACK"
        print("\n[ BOB ]:\t La Frase Segreta ricevuta dal Client è CORRETTA.")
    else:
        response = decifratura_textbook(encrypted,bob_d,bob_N)
        print("\n[ BOB ]:\t La Frase Segreta ricevuta dal Client è ERRATA.")
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)

