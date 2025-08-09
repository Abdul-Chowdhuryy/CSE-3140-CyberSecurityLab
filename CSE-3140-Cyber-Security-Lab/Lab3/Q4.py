from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

with open('/home/cse/Lab3/Q4files/Encrypted4', 'rb') as et:
    iv = et.read(16)
    encrypted_text = et.read()

with open('/home/cse/Lab3/Q4files/key.txt', 'rb') as key_file:
    key = key_file.read()

cipher = AES.new(key, AES.MODE_CBC, iv)
content = unpad(cipher.decrypt(encrypted_text), AES.block_size)
print('Decrypted content:', content.decode('utf-8'))