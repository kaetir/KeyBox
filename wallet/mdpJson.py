import json

with open("test.json", "r+") as f:
    content = f.read()
    jload = json.loads(content)
    jload["entries"].append({"username":"lui", "nonce" :"dbd4a82efcc7950b2d6ab1abafc0453b", "passwd" : "05fe5e"})

    f.seek(0)
    f.truncate(0)
    f.write(json.dumps(jload, indent=4).replace("    ",'\t'))    


