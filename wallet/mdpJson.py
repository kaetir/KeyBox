import json


def addEntry(file, application, username, nonce, passwd):
    with open(file, "r+") as f:
        content = f.read()
        jload = json.loads(content)
        jload["entries"].append({"application" : application,"username":username, "nonce" :nonce, "passwd" : passwd})
        f.seek(0)
        f.truncate(0)
        f.write(json.dumps(jload, indent=4).replace("    ",'\t'))    


def getEntries(file):
    with open(file, "r") as f:
        content = f.read()
        jload = json.loads(content)
        return jload["entries"]

def getEntry(file, application):
    with open(file, "r") as f:
        content = f.read()
        jload = json.loads(content)
        return [d for d in jload["entries"] if d["application"] == application ]


def genNewFile(filename, username, mainPasswdHash):
    with open(filename, "x") as f:
        jload = {"mainuser": username, 	"mainpasswd": mainPasswdHash, "entries": [] }
        f.write(json.dumps(jload, indent=4).replace("    ",'\t'))




