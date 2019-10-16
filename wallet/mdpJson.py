import json


def genNewFile(filename, username, mainPasswdHash):
    with open(filename, "x") as f:
        jload = {"mainuser": username, 	"mainpasswd": mainPasswdHash, "entries": [] }
        f.write(json.dumps(jload, indent=4).replace("    ",'\t'))
    
def addEntry(filename, application, username, nonce, passwd):
    with open(filename, "r+") as f:
        content = f.read()
        jload = json.loads(content)
        jload["entries"].append({"application" : application,"username":username, "nonce" :nonce, "passwd" : passwd})
        f.seek(0)
        f.truncate(0)
        f.write(json.dumps(jload, indent=4).replace("    ",'\t'))    


def getEntries(filename):
    with open(filename, "r") as f:
        content = f.read()
        jload = json.loads(content)
        return jload["entries"]

def getEntry(filename, application):
    with open(filename, "r") as f:
        content = f.read()
        jload = json.loads(content)
        return [d for d in jload["entries"] if d["application"] == application ][0]

def getUsername(filename):
       with open(filename, "r+") as f:
        content = f.read()
        jload = json.loads(content)
        return jload["username"]

def getHashedPasswwd(filename):
       with open(filename, "r+") as f:
        content = f.read()
        jload = json.loads(content)
        return jload["mainpasswd"]


