import os

os.chdir("/home/pi/Keybox")

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


def write_keybord(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())


menuWelcome.select()

# TODO Authentification
while ma_saisie.select_alphabet() != "":
    print("NOP")

while True:
    entre = menuPrincipal.select()
    # Menu comptes
    while entre == 0:
        compte_entre = menuComptes.select()
        if compte_entre == -1:
            break

    # Menu Wifi
    while entre == 1:
        wifi_entre = menuWifi.select()
        if wifi_entre == -1:
            break
        elif wifi_entre == 0:
            en_hostspot()
            print("OK")
        elif wifi_entre == 1:
            dis_hostspot()
        elif wifi_entre == 2:
            monEcran.clear_scr()
            monEcran.draw_text(get_wifi_passwd(), 0)
            monEcran.display()
            mesBoutons.while_pressed("OK", 5000)
            while mesBoutons.getStatus("OK"):
                print("TODO")
            mesBoutons.while_pressed("OK", 60000)
    # test clavier
    if entre == 2: # Non bloquant
        NULL_CHAR = chr(0)
        # Press c key
        write_report(NULL_CHAR * 2 + chr(6) + NULL_CHAR * 5)
        # Press a
        write_report(NULL_CHAR * 2 + chr(4) + NULL_CHAR * 5)
        # Release keys
        write_report(NULL_CHAR * 8)
        # Press c key
        write_report(NULL_CHAR * 2 + chr(6) + NULL_CHAR * 5)
        # Press a
        write_report(NULL_CHAR * 2 + chr(4) + NULL_CHAR * 5)
        # Release keys
        write_report(NULL_CHAR * 8)