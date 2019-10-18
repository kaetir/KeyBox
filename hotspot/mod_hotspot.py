from os import system

def new_passwd_hotspot():
    system("python3 edit_hostapd_conf.py")

def en_hostspot():
    new_passwd_hotspot()
    system("systemctl start hostapd")

def dis_hostspot():
    system("systemctl stop hostapd")

def get_wifi_passwd():
    with open("/etc/hostapd/hostapd.conf","r+") as f:
        content = f.read()
        data = content.split("\n")[:-1]
        dic = {x.split("=")[0] : x.split("=")[-1] for x in data}   
        return dic["wpa_passphrase"] 