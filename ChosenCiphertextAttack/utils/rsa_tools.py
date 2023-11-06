import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

'''
    Funzioni per PublicKey e Private Key
'''
#Genera coppia di chiavi
def generate_key_pair(size, public_exponent):
    private_key = rsa.generate_private_key(
        public_exponent=public_exponent,
        key_size=size,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

#Estrazione (e,N) da Public Key
def publickey_parameters(public_key):
    public_numbers = public_key.public_numbers()
    e = public_numbers.e
    n = public_numbers.n
    return e, n

#Estrazione (d,N) da Private Key
def privatekey_parameters(private_key):
    private_numbers = private_key.private_numbers()
    d = private_numbers.d
    n = private_numbers.public_numbers.n
    return d, n

'''
    Funzioni per Cifrare e Decifrare
    RSA Textbook
'''
# Cifra testo con Textbook RSA (NO PADDING)
def encrypt_textbookRSA(string,e,N):
    int_string = testo_a_intero(string)                 # Converte testo -> intero
    encrypted  = cifratura_textbook(int_string,e,N)     # Cifra intero - operazione aritmetica
    return encrypted

# Decifra testo cifrato con Textbook RSA (NO PADDING)
def decrypt_textbookRSA(int_number,d,N):
    string_int = intero_a_testo(int_number)             # Converte intero -> testo
    decrypted = decifratura_textbook(string_int,d,N)    # Decifra intero - operazione aritmentica
    return decrypted

#Encrypt - Operazione algebrica
def cifratura_textbook(M, e, N):
    cipher = M ** e % N         # operazione di cifratura: (M^e) mod_N
    return cipher

#Decrypt - Operazione algebrica
def decifratura_textbook(C,d,N):
    decipher = pow(C, d , N)    # operazione di decifratura: (C^d) mod_N
    return decipher

#Conversione Testo->Intero
def testo_a_intero(testo):
    testo_codificato = base64.b64encode(testo.encode('utf-8'))  # Converte la stringa in una sequenza di byte codificata in base64.
    intero = int.from_bytes(testo_codificato, byteorder='big')  # Converte la sequenza di byte codificata in base64 in un intero 
    return intero

#Conversione Intero->Testo
def intero_a_testo(intero):
    testo_codificato = intero.to_bytes((intero.bit_length() + 7) // 8, byteorder='big') # Calcola il numero di byte necessari e converte l'intero in una sequenza di byte
    testo = base64.b64decode(testo_codificato).decode('utf-8')                          # Converte la sequenza di byte in una stringa
    return testo
