
# encrypt with CBC, padding and remove padding functions 

# Author : Elisabeth Oswald (elisabeth.oswald@aau.at) and Arnab Roy (arnab.roy@aau.at)

import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding



class padding_oracle:

	key = b"0"
	iv = b"0"

	def __init__(self, k, IV):
		self.key = k
		self.iv = IV

	def pad(self, s):
		padder = padding.PKCS7(128).padder()
		s = padder.update(s) + padder.finalize()
		return s

	def unpad(self, s):
		unpadder = padding.PKCS7(128).unpadder()
		s = unpadder.update(s) + unpadder.finalize()
		return s
    	#return s

	def encrypt(self, msg):
		pmsg = self.pad(msg)
		cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv))
		encrypt = cipher.encryptor()
		ct = encrypt.update(pmsg) + encrypt.finalize()
		return ct

	def decrypt(self,ct):
		cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv))
		decrypt = cipher.decryptor()
		pmsg = decrypt.update(ct) + decrypt.finalize()
		return self.unpad(pmsg)



def main():

	iv = b"0123456789012345"
	key =b"0123456789012345"

	plaintext =b"hidetestmessage"

	print(f"Simple sanity checks for encryption/decryption, padding and unpadding")

	print(f"IV = {iv.hex()}, length = {len(iv)}")
	print(f"Key = {key.hex()}, length = {len(key)}")
	print(f"plaintext = {plaintext.hex()}, length = {len(plaintext)}")

	p = padding_oracle(key, iv)

	padded_text = p.pad(plaintext)

	print(f"padded plaintext = {padded_text.hex()}, length = {len(padded_text)}")


	ct = p.encrypt(plaintext)

	print(f"ciphertext = {ct.hex()}, legth = {len(ct)}")

	ciphertextwithIV = b"".join([iv, ct])

	print(f"ciphertext = {ciphertextwithIV.hex()}, legth = {len(ciphertextwithIV)}")

	p = p.decrypt(ct)

if __name__ == "__main__":

	main()