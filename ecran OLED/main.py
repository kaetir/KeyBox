
from boutons import Boutons
from ecran import Ecran
from menu  import Menu

monEcran = Ecran()
mesBoutons = Boutons()
monMenu = Menu(monEcran, mesBoutons)
menuLogin = Menu(monEcran, mesBoutons, "login.txt")

"""
# on efface et on affiche un texte
monEcran.clear_scr()
monEcran.draw_text("TEST1", 0, 1)

# on réefface et on affiche un autre texte
#monEcran.clear_scr()
monEcran.draw_text("TEST2", 1, 6)
"""



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
print(monMenu.entries[monMenu.select()])


