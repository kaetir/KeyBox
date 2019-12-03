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

    def print(self, counter=-1) -> None:
        """
        @summary affiche le menu
        @param counter: int -> position du curseur si -1 pas affiché
        """
        self.ecran.clear_scr()
        self.ecran.draw_text(self.title, 0)
        self.ecran.draw_text(">",3)
        for i in range(len(self.entries)):
            self.ecran.draw_text(str(i+1) + ". " + self.entries[i], i + 1)
        if counter >= 0:
            self.ecran.curs(1,counter)
        self.ecran.display()
    
    
    def select(self) -> int:
        """
        @summary lit l'état des boutons jusqu'a ce que OK ou BACK soit préssé
        @return  -1 si BACK
        @return  numéro de l'entré si OK 
        """
        self.print()
        counter=0
        while True:
            if self.boutons.getStatus("UP")==False:
                counter+=1
                self.print(counter)
                while self.boutons.getStatus("UP")==False:
                    self.boutons.getStatus("UP")
                
            elif self.boutons.getStatus("DOWN")==False:
                counter-=1
                self.print(counter)
                while self.boutons.getStatus("DOWN")==False:
                    self.boutons.getStatus("DOWN")
            elif self.boutons.getStatus("OK")==False :
                return counter
            elif self.boutons.getStatus("BACK")==False:
                counter=-1
                return counter