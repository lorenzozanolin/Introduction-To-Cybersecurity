import string

def encrypt_letter(letter, key): 
    return key[ord(letter) - ord('A')]


def encrypt_message(message, key):
    message = message.upper()
    cipher = ''
    for letter in message:
        if letter not in '\n- ,.:\'’':
            cipher += encrypt_letter(letter, key)
        else:
            cipher += letter
    return cipher

def keyRecovery(key,plain,cipher,i, length):
    if i==length: 
        key = ''.join(key)
        print(key)
        if(encrypt_message(plain,key) == cipher):
            return key
    else:
        for j in range(i,length):
            #swap
            key[i], key[j] = key[j], key[i] 
            keyRecovery(key,plain,cipher, i+1, length) 
            key[i], key[j] = key[j], key[i]
  

text = "This is some random text, please replace with whatever you see fit."
k = "GPRNUBIYKFEZMWXVDTJOHLSQCA"

letters = list(string.ascii_uppercase)

ciphertext = encrypt_message(text, k)



print(f"Plaintext: {text}")
print(f"Encryption key: {k}")
print(f"Ciphertext: {ciphertext}")
print(f"Key recovered: {keyRecovery(letters,text,ciphertext,0,len(letters))}")
