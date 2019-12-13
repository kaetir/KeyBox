
from ecran.boutons import Boutons
from ecran.ecran import Ecran
from ecran.menu  import Menu
from ecran.alphabet import Alphabet
from hotspot.mod_hotspot import *

monEcran = Ecran()
mesBoutons = Boutons()
#monMenu = Menu(monEcran, mesBoutons)
menuComptes = Menu(monEcran, mesBoutons,"ecran/Comptes.txt")
menuPrincipal = Menu(monEcran, mesBoutons,"ecran/menuPrincipal.txt")
menuWifi = Menu(monEcran, mesBoutons,"ecran/hotspot.txt")
menuWelcome = Menu(monEcran, mesBoutons, "ecran/Welcome.txt")
ma_saisie = Alphabet(monEcran, mesBoutons)


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
            change_wifi_passwd()
            print("OK")
        elif wifi_entre  ==1:
            get_wifi_passwd()
