import os
import bcrypt

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CTR
from cryptography.hazmat.backends import default_backend

from Crypto.Hash import SHA512


def mdp_crypt(main_password, password_to_crypt):
    """
    @param main_password: str -> the userpassword
    @param password_to_crypt: str -> to crypt
    @return: byte string
    """
    nonce = os.urandom(16)
    key = bcrypt.kdf(password=bytes(main_password, "utf8"), salt=nonce, desired_key_bytes=32, rounds=100)
    ciph = Cipher(AES(key), CTR(nonce), default_backend())
    encryptor = ciph.encryptor()

    return encryptor.update(bytes(password_to_crypt, "utf8")).hex(), nonce.hex()


def mdp_decrypt(main_password: str, pasword_to_decrypt: bytes, nonce: bytes) -> str:
    """
    @summary décrypte un mot de passe a partir du maitre et du nonce
    @param main_password: str
    @param pasword_to_decrypt: byte string
    @param nonce:
    @return: str
    """
    key = bcrypt.kdf(password=bytes(main_password, "utf8"), salt=bytes.fromhex(nonce), desired_key_bytes=32, rounds=100)
    ciph = Cipher(AES(key), CTR(bytes.fromhex(nonce)), default_backend())
    decryptor = ciph.decryptor()

    return decryptor.update(bytes.fromhex(pasword_to_decrypt)).decode("utf8")


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
