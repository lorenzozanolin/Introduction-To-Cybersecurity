from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

#--------------     RSAOAEP
def encrypt_RSA_OAEP(message,public_key):
    return public_key.encrypt(message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))

def decrypt_RSA_OAEP(ciphertext,private_key):
    return private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    
def generate_keys():   
    #private_key, public_key
    private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    )
    return private_key,private_key.public_key()

private,public = generate_keys()
cipher = encrypt_RSA_OAEP(b"This is a test",public)
plain = decrypt_RSA_OAEP(cipher,private)

#print(cipher)
#print(plain)



#--------------     HYBRID

# ASYMMETRIC PART
def encryption_KEM(public_key):
    #create the session_key (used for symmetric communication)
    cipher_key = encrypt_RSA_OAEP(os.urandom(32),public_key)    #128bit key
    return cipher_key

def decryption_KEM(private_key,crypted_key):
    plain_key = decrypt_RSA_OAEP(crypted_key,private_key)
    return plain_key

def createSymmetricCipher(session_key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(session_key), modes.CTR(iv))
    return cipher


# SYMMETRIC PART
def encryption_DEM(message,encryptor):
    ciphertext =  encryptor.update(message) + encryptor.finalize() 
    return ciphertext  

def decryption_DEM(ciphertext,decryptor):
    message = decryptor.update(ciphertext) + decryptor.finalize()
    return message
    
#KEM
private,public = generate_keys()
c1 = encryption_KEM(public)

#DEM
k = decryption_KEM(private,c1)
cipher = createSymmetricCipher(k)
encryptor = cipher.encryptor()
decryptor = cipher.decryptor()

msg = b"Hello world"
c2 = encryption_DEM(msg,encryptor)
#print(c2)
#print(decryption_DEM(c2,decryptor))





