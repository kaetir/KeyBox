#!/usr/bin/python3
from genRngPasswd import randomString

dic = {}

with open("/etc/hostapd/hostapd.conf","r+") as f:
    content = f.read()
    data = content.split("\n")[:-1]
    dic = {x.split("=")[0] : x.split("=")[-1] for x in data}   

with open("/etc/hostapd/hostapd.conf","w") as f:
    
    dic["wpa_passphrase"] = randomString(8)
    tamerelapute = [ "{}={}\n".format(key,dic[key]) for key in dic]
    print(tamerelapute)
    for l in tamerelapute:
        f.writelines(l)