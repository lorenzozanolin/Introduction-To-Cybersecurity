import string
from itertools import product

def encrypt_letter(letter, key):    #c = m − k (mod 26)
    return chr(ord('A') + (ord(letter) + ord(key)) % 26)
    
def decrypt_letter(letter, key):    #m = c + k (mod 26)
    return chr(ord('A') + (ord(letter) - ord(key)) % 26)
    
def encrypt_message(message, key):
    message = message.upper()
    key = key.upper()
    cipher = ''
    if len(message) != len(key):
        print(f"Message and key must be of equal length ... aborting.")
    else:
        for letter in range(len(message)):
            if message[letter] not in '\n- ,.:\'’':
                cipher += encrypt_letter(message[letter], key[letter])
            else:
                cipher += message[letter]

    return cipher

def decrypt_message(ciphertext, key):
    key = key.upper()
    message = ''
    if len(ciphertext) != len(key):
        print(f"Message and key must be of equal length ... aborting.")
    else:
        for letter in range(len(ciphertext)):
            if ciphertext[letter] not in '\n- ,.:\'’':
                message += decrypt_letter(ciphertext[letter],key[letter])
            else:
                message += ciphertext[letter]
    return message

def load_words():
    with open("words_alpha.txt") as word_file:
        valid_words = set(word_file.read().split()) 
    return valid_words

def createKeys(candidates):
    keys = []
    for i in range(len(candidates)):
        keys.append("".join(candidates[i]))
    return keys

def getIntersection(set1,set2):
    return set1 & set2
#----------------------------------------------------------------------------------------------------

english_words = load_words()
three_letter_words = [word for word in english_words if len(word) == 3]

keys = createKeys(list((product(list(string.ascii_lowercase),list(string.ascii_lowercase),list(string.ascii_lowercase)))))

plaintexts = []
ciphertext = "abc"

for i in range(len(keys)):
<<<<<<< HEAD
    plaintexts.append(decrypt_message(ciphertext,keys[i]).lower())))
=======
    plaintexts.append(decrypt_message(ciphertext,keys[i]))
>>>>>>> f31ca192c1326b42849f42449ae68b83dbde0b8a

intersection = getIntersection(set(plaintexts),set(three_letter_words))

print(list(intersection))
    

#ciphertext = encrypt_message("Ciao", secretkey)
#plaintextRecovered = decrypt_message(ciphertext,secretkey)

#print(f"[+] Plaintext: {plaintext}")
#print(f"[+] Secret Key: {secretkey}")
#print(f"[+] Ciphertext: {ciphertext}")
#print(f"[+] Recoverd: {plaintextRecovered}")
