
with open("/etc/hostapd/hostapd.conf","r+") as f:
    content = f.read()
    data = content.split("\n")
    dic = {x.split("=")[0] : x.split("=")[-1] for x in data}
    print(dic["wpa_passphrase"])
    



