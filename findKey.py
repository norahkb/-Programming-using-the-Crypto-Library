from Crypto.Cipher import AES
import os

def find_encryption_key(plaintext, ciphertext):
    with open('wordlist.txt') as f:
        wordlist = [word.strip() for word in f]

    for word in wordlist:
        key = (word + '#'*16)[:16]
        cipher = AES.new(key.encode(), AES.MODE_CBC, bytes.fromhex(iv))
        decrypted = cipher.decrypt(bytes.fromhex(ciphertext)).decode('latin-1')

        print(f"Trying key: {key}")
        print(f"Decrypted: {decrypted}")
        print(f"Plaintext: {plaintext}")

        if decrypted == plaintext:
            return key

    return None

plaintext = "This is a top secret"
ciphertext = "764aa26b55a4da654df6b19e4bce00f4"
iv = "aabbccddeeff00998877665544332211"

encryption_key = find_encryption_key(plaintext, ciphertext)

if encryption_key:
    print("Encryption Key found:", encryption_key)
else:
    print("Encryption Key not found.")
