
from boutons import Boutons
from ecran import Ecran
from menu  import Menu
from alphabet import Alphabet

monEcran = Ecran()
mesBoutons = Boutons()
#monMenu = Menu(monEcran, mesBoutons)
menuLogin = Menu(monEcran, mesBoutons,"login.txt")
menuWelcome = Menu(monEcran, mesBoutons, "Welcome.txt")
ma_saisie = Alphabet(monEcran, mesBoutons)

"""
# on efface et on affiche un texte
monEcran.clear_scr()
monEcran.draw_text("TEST1", 0, 1)

# on réefface et on affiche un autre texte
#monEcran.clear_scr()
monEcran.draw_text("TEST2", 1, 6)
"""


#monMenu.print()
#menuWelcome.print()
menuWelcome.select()

while ma_saisie.select_alphabet() != "caca":
    print("NOP")


menuLogin.select()
#menuLogin.print()

"""
while (monMenu.select()==1):
    monMenu.print()
    while monMenu.select()==0:
        menuLogin.print()
"""
# on a bien que le deuxieme texte qui d'affiche


#mesBoutons.test_mapping()
#test de mapping des boutons

#Menu des comptes avec sélection du compte
#print(monMenu.entries[monMenu.select()])


