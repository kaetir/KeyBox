from __future__ import annotations
import wallet.mdpJson as walletJson
from wallet.mdpCypher import *
from wallet.genRngPasswd import *

"""
gestion du wallet 

"""


class Wallet:
    def __init__(self, filename: str):
        """
        @summary constructeur
        @param filename: string du path du fichier
        """
        self.mainpassword = ""
        self.file = filename
        self.lock = True

    def unlock(self, mainpasswd: str) -> bool:
        """
        @summary unlock the wallet
        """
        if walletJson.check_valid(self.file, hash_function(mainpasswd)) >= 0:
            self.lock = False
            self.mainpassword = walletJson.get_main_key(self.file, hash_function(mainpasswd))
            return True
        return False

    def create_wallet(self, username: str, mainpasswd: str) -> str:
        """
        @summary crée le fichier du wallet
        @param username: str
        @param mainpasswd: str le mot de passe d'ouverture
        @return la clé de récupération du wallet
        """
        if walletJson.gen_new_file(self.file, username, hash_function(mainpasswd)) == 0:
            self.lock = False
            self.mainpassword = walletJson.get_main_key(self.file, hash_function(mainpasswd))
            security_sentence = gen_phrase()
            walletJson.add_password(self.file, hash_function(mainpasswd), hash_function(security_sentence))
            return security_sentence

    def add_password(self, actual_valid_password: str, new_password: str) -> bool:
        """
        @summary add a password to the wallet
        @param actual_valid_password: str an actual valid password for the wallet
        @param new_password: str the new password to unlock the wallet
        @return: bool succeed
        """
        return walletJson.add_password(self.file, hash(actual_valid_password), hash_function(new_password))

    def get_acount(self, application: str) -> Optional[bool, dict]:
        """
        @summary récupere un compte en clair
        @param application: the name of the acount you want to get
        @param mainpasswd: the mainpassword of the user
        @return: dict an acount with all is informations
        """
        if self.lock:
            return False

        if walletJson.get_entry(self.file, application):
            entry = walletJson.get_entry(self.file, application)
            entry["passwd"] = mdp_decrypt(self.mainpassword, entry["passwd"], entry["nonce"])
            return entry

    def get_applications(self) -> Optional[bool, list]:
        """
        @summary récupere la liste des comptes
        @return: dict an acount with all is informations
        """
        if self.lock:
            return False

        entries = walletJson.get_entries(self.file)
        if entries is not False:
            return [e["application"] for e in entries]
        else:
            print("WRONG PASSWORD")
            return False

    def create_acount(self, application: str, username: str, passwd: str, mainpasswd: str) -> bool:
        """
        @summary creating an account in the file in parametre
        @param application: str the name of the application
        @param username: str the username
        @param passwd: str the password of the acount
        @param mainpasswd: str the password of the wallet
        """

        if self.lock:
            if not self.unlock(mainpasswd):
                return False


        [mdpc, nonce] = mdp_crypt(self.mainpassword, passwd)
        return walletJson.add_entry(self.file, application, username, nonce, mdpc)


# def get_username(filename, passwd):


if __name__ == "__main__":
    wallet_file = "test.json"
    w = Wallet(wallet_file)
    mainpasswd = input("mainpassword : ")
    # os.system("rm " + wallet_file)
    if not os.path.isfile(wallet_file):
        print("Creating a wallet")
        name = input("name : ")
        print("phrase de récup :", w.create_wallet(name, mainpasswd))

    while not w.unlock(mainpasswd):
        mainpasswd = input("mainpassword : ")

    if "o" == input("open wallet for reading (o/N)? :"):
        print(w.get_applications())
        application = input("application : ")
        print(w.get_acount(application))
    else:
        print("add an entry")
        application = input("application : ")
        user = input("username : ")
        passwd = input("password : ")

        w.create_acount(application, user, passwd, mainpasswd)
