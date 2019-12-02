
from boutons import Boutons
from ecran import Ecran

monEcran = Ecran()

# on efface et on affiche un texte
monEcran.clear_scr()
monEcran.draw_text("TEST1", 0, 1)

# on réefface et on affiche un autre texte
#monEcran.clear_scr()
monEcran.draw_text("TEST2", 1, 6)

# on a bien que le deuxieme texte qui d'affiche
monEcran.display()
