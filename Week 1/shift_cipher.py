def encrypt_letter(letter, key):
    return chr(ord('A') + (ord(letter) - ord('A') + key) % 26)


def encrypt_message(message, key):
    message = message.upper()
    cipher = ''
    for letter in message:
        if letter not in ' ,.':
            cipher += encrypt_letter(letter, key)
        else:
            cipher += letter
    return cipher

#for a given key, try to encrypt the message and check wheter it is equal to the original message
def keyRecovery(plain,cipher):
    k = -25
    cipher2 = ""
    while cipher2 != cipher:
        cipher2 = encrypt_message(plain,k)
        if cipher2 == cipher:
            return k
        k +=1

text = "This is some random text, please replace with whatever you see fit."

k=-4

ciphertext = encrypt_message(text, k)

print(f"Plaintext: {text}")
print(f"Ciphertext: {ciphertext}")

print(f"Recovered: {encrypt_message(ciphertext,-keyRecovery(text,ciphertext))}")