#!/usr/bin/python3
import os

os.chdir("/home/pi/Keybox")
os.system("hostname -I > ip.txt")

from ecran.boutons import Boutons
from ecran.ecran import Ecran
from ecran.menu import Menu
from ecran.alphabet import Alphabet
from hotspot.mod_hotspot import *

from wallet.wallet import Wallet

monEcran = Ecran()
mesBoutons = Boutons()
# monMenu = Menu(monEcran, mesBoutons)
menuComptes = Menu(monEcran, mesBoutons, "ecran/Comptes.txt")
menuPrincipal = Menu(monEcran, mesBoutons, "ecran/menuPrincipal.txt")
menuWifi = Menu(monEcran, mesBoutons, "ecran/hotspot.txt")
menuWelcome = Menu(monEcran, mesBoutons, "ecran/Welcome.txt")
ma_saisie = Alphabet(monEcran, mesBoutons)

menuWelcome.select()

fileWallet = "wallet.json"
w = Wallet(fileWallet)

if not os.path.isfile(fileWallet):
    monEcran.clear_scr()
    monEcran.draw_text("Creer un wallet avec", 0)
    monEcran.draw_text("l'interface web", 1)
    monEcran.display()
    mesBoutons.while_pressed("OK", 5000)
    while mesBoutons.getStatus("OK"):
        pass
    mesBoutons.while_pressed("OK", 60000)
    # activation du wifi 
    en_hostspot()
    monEcran.clear_scr()
    monEcran.draw_text(open("ip.txt").read(), 0)
    monEcran.draw_text(get_wifi_passwd(), 1)
    monEcran.display()
    exit(0)
    
# Authentification
while w.unlock(ma_saisie.select_alphabet()):
    print("NOP")

while True:
    entre = menuPrincipal.select()
    # Menu comptes
    while entre == 0:
        compte_entre = menuComptes.select()
        if compte_entre == -1:
            break
        else:
            monEcran.clear_scr()
            #w 
            monEcran.draw_text(socket.gethostbyname(socket.gethostname()), 0)
            monEcran.draw_text(get_wifi_passwd(), 1)
            monEcran.display()
            mesBoutons.while_pressed("OK", 5000)
            while mesBoutons.getStatus("OK"):
                pass
            mesBoutons.while_pressed("OK", 60000)
            

    # Menu Wifi
    while entre == 1:
        wifi_entre = menuWifi.select()
        if wifi_entre == -1:
            break
        # activer hotspot
        elif wifi_entre == 0:
            en_hostspot()
            wifi_entre = 2
        # desactiver hotspot
        elif wifi_entre == 1:
            dis_hostspot()
        
        # afficher mot de passe
        if wifi_entre == 2:
            monEcran.clear_scr()
            monEcran.draw_text(open("ip.txt").read(), 0)
            monEcran.draw_text(get_wifi_passwd(), 1)
            monEcran.display()
            mesBoutons.while_pressed("OK", 5000)
            while mesBoutons.getStatus("OK"):
                pass
            mesBoutons.while_pressed("OK", 60000)
    