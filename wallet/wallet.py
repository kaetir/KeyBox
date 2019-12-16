import mdpJson as walletJson
from mdpCypher import *

"""
gestion du wallet 

"""


def createWallet(filename: str, username: str, mainpasswd: str) -> str:
    """
    @summary crée le fichier du wallet
    @param filename: string du path du fichier
    @param username: object
    @param mainpasswd: le mot de passe d'ouverture
    @return la clé de récupération du wallet
    """
    walletJson.gen_new_file(filename, username, hash_function(mainpasswd))


def add_password(filename: str, actual_valid_password: str, new_password: str) -> bool:
    """
    @summary add a password to the wallet
    @param filename: str the file of the wallet
    @param actual_valid_password: str an actual valid password for the wallet
    @param new_password: str the new password to unlock the wallet
    @return: bool succeed
    """
    return walletJson.add_password(filename, actual_valid_password, hash_function(new_password))


def get_acount(filename: str, application: str, mainpasswd: str)-> dict:
    """
    @summary récupere un compte en clair
    @param filename: the file of the wallet
    @param application: the name of the acount you want to get
    @param mainpasswd: the mainpassword of the user
    @return: dict an acount with all is informations
    """
    if walletJson.get_entry(filename, application):
        entry = walletJson.get_entry(filename, application)
        entry["passwd"] = mdp_decrypt(mainpasswd, entry["passwd"], entry["nonce"])
        return entry
    else:
        print("WRONG PASSWORD")


def create_acount(filename: str, application: str, username: str, passwd: str, mainpasswd: str) -> None:
    """
    @summary creating an account in the file in parametre
    @param filename: str the file of the wallet
    @param application: str the name of the application
    @param username: str the username
    @param passwd: str the password of the acount
    @param mainpasswd: str the password of the wallet
    """
    if walletJson.check_valid(filename, hash_function(mainpasswd)) >= 0:
        [mdpc, nonce] = mdp_crypt(mainpasswd, passwd)
        walletJson.add_entry(filename, application, username, nonce, mdpc)
    else:
        print(hash_function(mainpasswd))
        print("WRONG PASSWORD")


# def get_username(filename, passwd):


if __name__ == "__main__":
    filename = "test.json"
    # os.system("rm " + filename)
    if not os.path.isfile(filename):
        print("Creating a wallet")
        name = input("name : ")
        mainpasswd = input("mainpassword : ")
        createWallet(filename, name, mainpasswd)
        recup = gen_phrase(10)

    if "o" == input("open wallet for reading (o/N)? :"):
        application = input("application : ")
        mainpasswd = input("mainpassword : ")
        print(get_acount(filename, application, mainpasswd))
    else:
        print("add an entry")
        application = input("application : ")
        user = input("username : ")
        passwd = input("password : ")
        mainpasswd = input("mainpassword : ")

        create_acount(filename, application, user, passwd, mainpasswd)
