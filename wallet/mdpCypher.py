

import os
import bcrypt

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CTR
from cryptography.hazmat.backends import default_backend


# mainpasswd = str of the userpasswd
# passToCrypt = str to crypt
# return = byte string  
def mdpCrypt(mainpasswd, passToCrypt):
    nonce = os.urandom(16)
    key = bcrypt.kdf( password=bytes(mainpasswd, "utf8"), salt=nonce, desired_key_bytes=32, rounds=100)
    Ciph = Cipher(AES(key), CTR(nonce), default_backend())
    Encryptor = Ciph.encryptor()
    
    return Encryptor.update(bytes(passToCrypt, "utf8")).hex() , nonce.hex()
  

# mainpasswd = str of the userpasswd
# passToDecrypt = byte string
# return String 
def mdpDecrypt(mainpasswd, passToDecrypt, nonce):
    key = bcrypt.kdf( password=bytes(mainpasswd, "utf8"), salt=bytes.fromhex(nonce), desired_key_bytes=32, rounds=100)
    Ciph = Cipher(AES(key), CTR(bytes.fromhex(nonce)), default_backend())
    Decryptor = Ciph.decryptor()

    return Decryptor.update(bytes.fromhex(passToDecrypt)).decode("utf8")


if __name__ == "__main__":
    mp = input("your passwd pleas :")
    if("c" == input("crypt(c) / decrypt(d) : ")):
        uc = input("the thing you want to crypt : ")
        print(mdpCrypt(mp, uc))
    else:
        c = input("the thing you want to decrypt : ")
        n = input("the associate nonce : ")
        print(mdpDecrypt(mp, c,n ))
