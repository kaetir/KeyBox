#!/usr/bin/python3

from os import system
from wallet.genRngPasswd import *

def change_wifi_passwd():
    dic = {}

    with open("/etc/hostapd/hostapd.conf","r+") as f:
        content = f.read()[:-1]
        data = content.split("\n")
        dic = {x.split("=")[0] : x.split("=")[-1] for x in data}   

    with open("/etc/hostapd/hostapd.conf","w") as f:
        dic["wpa_passphrase"] = random_string(8)
        tamerelapute = [ "{}={}\n".format(key,dic[key]) for key in dic]
        print(tamerelapute)
        for l in tamerelapute:
            f.writelines(l)


def en_hostspot():
    change_wifi_passwd()
    system("systemctl restart hostapd")


def dis_hostspot():
    system("systemctl stop hostapd")


def get_wifi_passwd():
    with open("/etc/hostapd/hostapd.conf","r+") as f:
        content = f.read()
        data = content.split("\n")[:-1]
        dic = {x.split("=")[0] : x.split("=")[-1] for x in data}   
        return dic["wpa_passphrase"]

