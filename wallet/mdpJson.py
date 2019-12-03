import json
from mdpCypher import *

"""
Gestion of the passwords is made in json files
with a mainkey which is deciphered for each demand of opening 
with a secondary key
====================
Gere le stockage du mot de passe dans des fichiers json 
avec une mainkey qui se fait déchiffré a chaque demande d'ouverture par une
clé secondaire
"""


def genNewFile(filename: str, username: str, main_password_hash):
    """
    @summary generate file for wallet
    @param filename: name of the file to create
    @param username: le nom d'utilisateur
    @param main_password_hash: la clé principale du mec hashé
    @return:
    """
    try:
        with open(filename, "x") as f:
            mainkey = mdp_crypt(main_password_hash, os.urandom(16))
            jload = {"mainuser": username,
                     "mainkeys": [{
                         "mainkey": mainkey[0],
                         "nonce": mainkey[1]
                     }],
                     "checkpasswd": [{
                         "check": mdpCrypt(main_password_hash, "concombre")[0],
                         "nonce": mdpCrypt(main_password_hash, "concombre")[1]
                     }],
                     "entries": []}
            f.write(json.dumps(jload, indent=4).replace("    ", '\t'))
    except IOError:
        print("erreur avec le fichier")


def check_valid(password: str) -> bool:
    """
    @summary check the validity of a password
    @param password: password to check
    @return: True if the password can unlock the wallet
    """
    try:
        with open(filename, "r+") as f:
            content = f.read()
            jload = json.loads(content)
            for key in jload["mainkey"]:
                for check in jload["checkpasswd"]:
                    if "concombre" == mdp_decrypt(mdpDecrypt(password, key["mainkey"],
                                                             key["nonce"]), check["check"], chech["nonce"]):
                        return True
    except IOError:
        return False
    return False


def add_password(filename: str, actual_valid_password: str, new_password_hash: str) -> bool:
    """
    @summary add a password to the wallet
    @param filename: name of the file of the wallet
    @param actual_valid_password: one of the actual password
    @param new_password_hash: the new password to add
    @return: True if the password can unlock the wallet
    """
    try:
        with open(filename, "r+") as f:
            content = f.read()
            jload = json.loads(content)
            mainkey = mdp_crypt(main_password_hash, os.urandom(16))
            # new_password_hash
            jload["mainkeys"].append({
                "mainkey": mainkey[0],
                "nonce": mainkey[1]
            })
            f.seek(0)
            f.truncate(0)
            f.write(json.dumps(jload, indent=4).replace("    ", '\t'))
    except IOError:
        return False
    return True


def add_entry(filename, application, username, nonce, passwd) -> bool:
    """
    @summary add an entry to the wallet
    @param filename: name of the file of the wallet
    @param application: one of the actual password
    @param username: the new password to add
    @param nonce: the nonce of the password ciphered with the main key
    @param passwd: the password ciphered with the main key
    @return: True if the the entry is added to the wallet
    """
    try:
        with open(filename, "r+") as f:
            content = f.read()
            jload = json.loads(content)
            jload["entries"].append({"application": application, "username": username, "nonce": nonce, "passwd": passwd})
            f.seek(0)
            f.truncate(0)
            f.write(json.dumps(jload, indent=4).replace("    ", '\t'))
    except IOError:
        return False
    return True


def getEntries(filename):
    with open(filename, "r") as f:
        content = f.read()
        jload = json.loads(content)
        return jload["entries"]


def getEntry(filename, application):
    with open(filename, "r") as f:
        content = f.read()
        jload = json.loads(content)
        return [d for d in jload["entries"] if d["application"] == application][0]


def getUsername(filename):
    with open(filename, "r+") as f:
        content = f.read()
        jload = json.loads(content)
        return jload["username"]


def getPasswordValidity(filename: str, passwdToCheck: str) -> bool:
    """
    @sumarry on ne garde plus le hash_function du mot de passe mais
            on déchiffre une valeur connue avec la clé déchiffré
    @param filename : le path du fichier de wallet 
    @param passwdToCheck le mot de passe que l'on veut vérifié
    """
    with open(filename, "r+") as f:
        content = f.read()
        jload = json.loads(content)
        jload["mainkey"]
