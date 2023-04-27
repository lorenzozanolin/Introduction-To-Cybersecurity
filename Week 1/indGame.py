from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def game_master_setup():
    print(f"[-] The game master sets up the encryption box ...")
    sk = get_random_bytes(16)
    EncBox = AES.new(sk, AES.MODE_ECB)
    return EncBox


def game_master_random_bit():
    b = (int.from_bytes(get_random_bytes(1), "big")) & 1
    return b


def adversary_naive():
    m0 = get_random_bytes(16)
    m1 = get_random_bytes(16)
    return m0, m1

def adversary_clever():
    m_a = get_random_bytes(16)
    m_b = get_random_bytes(16)
    
    m0 = m_a + m_a
    m1 = m_a + m_b
    
    return m0,m1


print(f"Starting the IND game ...")
print(f"Setting up the game ...")
EncryptionOracle = game_master_setup()
secretbit = game_master_random_bit()

print(f"[-] The adversary produces two messages m0 and m1 ...")
#m0, m1 = adversary_naive()
m0,m1 = adversary_clever()
print(f"[-] Plaintext m0: {m0.hex()}")
print(f"[-] Plaintext m1: {m1.hex()}")



print(f"[-] The game master samples a random bit  and encrypts one of the two messages. ")

if secretbit == 0:
    c = EncryptionOracle.encrypt(m0)
else:
    c = EncryptionOracle.encrypt(m1)


print(f"[-] Now you are the adversary. Which plaintext corresponds to the ciphertext {c.hex()} ?")

guessb = int(input("Enter your guess for the secret bit b:  "))
print(f"[-] Your guess is: {guessb} and the secret bit is {secretbit}")
if secretbit == guessb:
    print(f"You got lucky!")
else:
    print(f"You loose, try again!")