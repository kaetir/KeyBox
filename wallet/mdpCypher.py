

import os
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.modes import CTR

AES.block_size = 256

nonce = os.urandom(32)
k = os.urandom(16)

m = b"Le caca c'est delicieux."


Cipher = Cipher(AES(k), CTR(nonce), default_backend())
Encryptor = Cipher.encryptor()
Decryptor = Cipher.decryptor()

gc = Encryptor.update(m)
print(gc.hex())
    

print(Decryptor.update(gc))

