## implement CBC mode
## 
import base64
from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long, long_to_bytes

IV = b'\x00' * 16
key = b"YELLOW SUBMARINE"

def encrypt_ecb_128(text):
   return AES.new(key, AES.MODE_ECB).encrypt(text)

def decrypt_ecb_128(ciphertext):
    return AES.new(key,AES.MODE_ECB).decrypt(ciphertext)

def xor_bytes(val1, val2):
    return long_to_bytes(bytes_to_long(val1) ^ bytes_to_long(val2))
        

with open('10.txt','r') as file:
    content = base64.b64decode(file.read())

blocks = b''
start = 0
previous_cipher = IV

for x in range(0, len(content), 16):
    chunks = content[x:x+16]
    decrypted = decrypt_ecb_128(chunks)
    val = xor_bytes(decrypted, previous_cipher)
    blocks += val
    previous_cipher = chunks

print(blocks.decode('utf-8'))
