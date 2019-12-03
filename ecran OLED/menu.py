from boutons import Boutons
from ecran import Ecran


class Menu():

    def __init__(self, ecran: Ecran, boutons: Boutons, fichier: str ="fichier.txt") -> None:
        """
        @summary constructeur
        @param ecran: Ecran -> réference sur l'écran
        @param boutons: Boutons -> références sur l'objets boutons$
        @param fichier: str -> fichier avec les entrés du menu
        """
        super().__init__()
        self.ecran = ecran
        self.boutons = boutons
        f = open(fichier, "r")
        content = f.read()
        data = content.split("\n")
        self.title = data[0]
        self.entries = data[1:]

    def print(self) -> None:
        """
        @summary affiche le menu
        """
        self.ecran.draw_text(self.title, 0)
        for i in range(len(self.entries)):
            self.ecran.draw_text(str(i+1) + ". " + self.entries[i], i + 1)
    
    
    def select(self) -> int:
        """
        @summary lit l'état des boutons jusqu'a ce que OK ou BACK soit préssé
        @return  -1 si BACK
        @return  numéro de l'entré si OK 
        """

