import os
import bcrypt

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CTR
from cryptography.hazmat.backends import default_backend

from Crypto.Hash import SHA512

AES.block_size = 256


def mdp_crypt(main_password: str, password_to_crypt: str):
    """
    @param main_password: str -> the userpassword
    @param password_to_crypt: str -> to crypt
    @return: byte string
    """
    nonce = os.urandom(32)
    key = bcrypt.kdf(password=bytes(main_password, "utf8"), salt=nonce, desired_key_bytes=32, rounds=100)
    ciph = Cipher(AES(key), CTR(nonce), default_backend())
    encryptor = ciph.encryptor()

    return encryptor.update(bytes(password_to_crypt, "utf8")).hex(), nonce.hex()


def mdp_decrypt(main_password: str, pasword_to_decrypt: str, nonce: str) -> str:
    """
    @summary décrypte un mot de passe a partir du maitre et du nonce
    @param main_password: str
    @param pasword_to_decrypt: str
    @param nonce: str
    @return: bytes .decode("utf8") pour utf8
    """
    nonce = bytes.fromhex(nonce)
    main_password = bytes(main_password, 'utf8')
    key = bcrypt.kdf(password=main_password, salt=nonce, desired_key_bytes=32, rounds=100)
    ciph = Cipher(AES(key), CTR(nonce), default_backend())
    decryptor = ciph.decryptor()

    return decryptor.update(bytes.fromhex(pasword_to_decrypt))


def hash_function(to_hash: str) -> str:
    """
    @summary fonction de hash_function simplifié
    @param to_hash: la chaine en clair
    @return: le hash_function digéré
    """
    return SHA512.new(bytes(to_hash, 'utf8')).hexdigest()


if __name__ == "__main__":
    mp = input("your passwd pleas :")
    if "c" == input("crypt(c) / decrypt(d) : "):
        uc = input("the thing you want to crypt : ")
        print(mdp_crypt(mp, uc))
    else:
        c = input("the thing you want to decrypt : ")
        n = input("the associate nonce : ")
        print(mdp_decrypt(mp, c, n))
