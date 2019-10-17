
import mdpJson as walletJson
from  mdpCypher import hash, mdpCrypt, mdpDecrypt, os


def createWallet(filename, username, mainpasswd):
    walletJson.genNewFile(filename, username, hash(mainpasswd).hexdigest())


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
        walletJson.addEntry(filename,application, username, nonce, mdpc)
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



