import mdpJson as walletJson
from  mdpCypher import *

"""


"""


def createWallet(filename: str, username: str, mainpasswd: str) -> str:
    """
    @summary crée le fichier du wallet
    @param filename: string du path du fichier
    @param username: object
    @param mainpasswd: le mot de passe d'ouverture
    @return la clé de récupération du wallet
    """
    walletJson.genNewFile(filename, username, hash(mainpasswd))


def getAcount(filename, application, mainpasswd):
    if(hash(mainpasswd).hexdigest() == walletJson.getHashedPasswwd(filename)):
        entry = walletJson.getEntry(filename,application)
        entry["passwd"] = mdpDecrypt(mainpasswd, entry["passwd"], entry["nonce"])
        return entry
    else:
        print("WRONG PASSWORD")

def createAcount(filename, application, username, passwd, mainpasswd):
    if(hash(mainpasswd).hexdigest() == walletJson.getHashedPasswwd(filename)):
        [mdpc, nonce] = mdpCrypt(mainpasswd, passwd)
        walletJson.add_entry(filename, application, username, nonce, mdpc)
    else:
        print(hash(mainpasswd).hexdigest())
        print( walletJson.getHashedPasswwd(filename))
        print("WRONG PASSWORD")




#def getUsername(filename, passwd):
    





if __name__ == "__main__":
    filename = "test.json"
    if(not os.path.isfile(filename) ):
        name =  input("name : ")
        mainpasswd = input("mainpassword : ")
        createWallet(filename,name, mainpasswd)
    
    if("o" == input("open wallet ? :")):
        application = input("application : ")
        mainpasswd  = input("mainpassword : ")
        print(getAcount(filename, application, mainpasswd))

    else:
        print("add an entry")
        application = input("application : ")
        user        = input("username : ")
        passwd      = input("password : ")
        mainpasswd  = input("mainpassword : ")

        createAcount(filename, application, user, passwd, mainpasswd)



