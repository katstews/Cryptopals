## file is encoded with aes-128-ecb, the key is 16 bytes
## thus need to divide ciphertext into blocks of 16, or 128 bits
## i didnt even need to break this into blocks of 16 bytes bruh
import base64
from Crypto.Cipher import AES

KEY = b"YELLOW SUBMARINE"

with open('7.txt','r') as file:
    content = base64.b64decode(file.read().strip())

plaintext = AES.new(KEY, AES.MODE_ECB).decrypt(content).decode('utf-8')

print(plaintext)

