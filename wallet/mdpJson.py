import json

"""
Gere le stockage du mot de passe dans des fichiers json 
avec une mainkey qui se fait déchiffré a chaque demande d'ouverture par une
clé secondaire

"""

def genNewFile(filename, username, mainkey, passwd):
	try :
		with open(filename, "x") as f:
			jload = {"mainuser": username, 	"mainkey": [mainPasswdHash, "entries": [] }
			f.write(json.dumps(jload, indent=4).replace("    ",'\t'))
	except IOError:
		print("erreur avec le fichier")
		
def add_entry(filename, application, username, nonce, passwd):
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

def getPasswordValidity(filename: str, passwdToCheck: str)-> bool:
	"""
	@sumarry on ne garde plus le hash du mot de passe mais 
 			on déchiffre une valeur connue avec la clé déchiffré
    @param filename : le path du fichier de wallet 
    @param passwdToCheck le mot de passe que l'on veut vérifié
	"""
	with open(filename, "r+") as f:
		content = f.read()
		jload = json.loads(content)
		 jload["mainkey"]
	


