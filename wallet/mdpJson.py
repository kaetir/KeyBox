from __future__ import annotations
import json
from wallet.mdpCypher import *

"""
Gestion of the passwords is made in json files
with a mainkey which is deciphered for each demand of opening 
with a secondary key
====================
Gere le stockage du mot de passe dans des fichiers json 
avec une mainkey qui se fait déchiffré a chaque demande d'ouverture par une
clé secondaire
"""


def gen_new_file(filename: str, username: str, main_password_hash) -> int:
    """
    @summary generate file for wallet
    @param filename: name of the file to create
    @param username: le nom d'utilisateur
    @param main_password_hash: la clé principale du mec hashé
    """
    try:
        with open(filename, "x") as f:
            mainkey_rng = os.urandom(32).hex()
            mainkey = mdp_crypt(main_password_hash, mainkey_rng)
            concombre = mdp_crypt(mainkey_rng, "concombre")
            #  alors la je suis con quand on appel la fonction on genere un nouveau nonce
            jload = {"mainuser": username,
                     "mainkeys": [{
                         "mainkey": mainkey[0],
                         "nonce": mainkey[1]
                     }],
                     "checkpasswd": {
                         "check": concombre[0],
                         "nonce": concombre[1]
                     },
                     "entries": []}
            f.write(json.dumps(jload, indent=4).replace("    ", '\t'))
    except IOError:
        print("erreur avec le fichier")
        return 1
    return 0


def check_valid(filename: str, main_password_hash) -> int:
    """
    @summary check the validity of a password using the "concombre"
    @param filename: file of the wallet
    @param main_password_hash: password to check
    @return: int: the position of the password which can unlock the wallet
            -1 if not found or error
    """
    try:
        with open(filename, "r") as f:
            content = f.read()
            jload = json.loads(content)
            for key in jload["mainkeys"]:
                try:
                    if "concombre" == mdp_decrypt(
                            mdp_decrypt(str(main_password_hash), str(key["mainkey"]), str(key["nonce"])).decode("utf8"),
                            jload["checkpasswd"]["check"], jload["checkpasswd"]["nonce"]).decode("utf8"):
                        return jload["mainkeys"].index(key)
                except UnicodeDecodeError:
                    pass
    except IOError:
        return -1
    return -1


def add_password(filename: str, actual_valid_password_hash: str, new_password_hash: str) -> bool:
    """
    @summary add a password to the wallet
    @param filename: name of the file of the wallet
    @param actual_valid_password_hash: one of the actual password
    @param new_password_hash: the new password to add
    @return: True if the password is added the wallet
    """
    valid_idx = check_valid(filename, actual_valid_password_hash)
    if valid_idx < 0:
        return False
    # actual_valid_password is valid
    try:
        with open(filename, "r+") as f:
            content = f.read()
            jload = json.loads(content)

            # Getting the main key of the wallet
            key = jload["mainkeys"][valid_idx]
            # the one that cypher the passwords
            mainkey = mdp_decrypt(actual_valid_password_hash, str(key["mainkey"]), str(key["nonce"])).decode("utf8")
            new_mainkey = mdp_crypt(new_password_hash, mainkey)

            jload["mainkeys"].append({
                "mainkey": new_mainkey[0],
                "nonce": new_mainkey[1]
            })
            f.seek(0)
            f.truncate(0)
            f.write(json.dumps(jload, indent=4).replace("    ", '\t'))
    except UnicodeDecodeError:
        return False
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
            jload["entries"].append(
                {"application": application, "username": username, "nonce": nonce, "passwd": passwd})
            f.seek(0)
            f.truncate(0)
            f.write(json.dumps(jload, indent=4).replace("    ", '\t'))
    except IOError:
        return False
    return True


def get_entries(filename: str) -> Optional[bool, dict]:
    """
    @summary  return all entrie from a file
    @param filename: name of the file of the wallet
    @return list[dict] :
    """
    try:
        with open(filename, "r") as f:
            content = f.read()
            jload = json.loads(content)
            return jload["entries"]
    except IOError:
        return False


def get_entry(filename: str, application: str):
    """
    @summary return an entrie from a file if multiple for the application return the first
    @param filename: str -> name of the file of the wallet
    @param application: str ->  the name of the application we want the password
    @return dict : entry ->   "application"    "username"    "nonce"    "passwd"
    """
    try:
        with open(filename, "r") as f:
            content = f.read()
            jload = json.loads(content)
            for entry in jload["entries"]:
                if entry["application"] == application:
                    return entry
    except json.JSONDecodeError:
        print("Mauvais format de json")
        exit(-1)
    return ""


def get_username(filename: str) -> None:
    """
    @summary return the username of a file
    @param filename: str -> name of the file of the wallet
    @return str : le pseudo de l'utilisateur
    """
    with open(filename, "r") as f:
        content = f.read()
        jload = json.loads(content)
        return jload["username"]


def get_main_key(filename: str, password_hash: str) -> Optional[bool, str]:
    """
    @summary return the mainkey to cypher the passwords
    @param filename: file of the wallet
    @param password_hash: password to check
    @return: str the main key or false if not a good password
    """
    valid_idx = check_valid(filename, password_hash)
    if valid_idx < 0:
        return False
    with open(filename, "r") as f:
        content = f.read()
        jload = json.loads(content)

        # Getting the main key of the wallet
        key = jload["mainkeys"][valid_idx]
        # Celle qui chiffre les mots de passe
        mainkey = mdp_decrypt(password_hash, str(key["mainkey"]), str(key["nonce"])).decode("utf8")

        return mainkey
