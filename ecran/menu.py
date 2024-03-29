from ecran.boutons import Boutons
from ecran.ecran import Ecran


class Menu:

    def __init__(self, ecran: Ecran, boutons: Boutons, file: str = "vide.txt", entres: list = None) -> None:
        """
        @summary constructeur
        @param ecran: Ecran -> réference sur l'écran
        @param boutons: Boutons -> références sur l'objets boutons$
        @param file: str -> file avec les entrés du menu
        @param entres: list -> overwrite the file entries
        """
        super().__init__()
        self.ecran = ecran
        self.boutons = boutons
        self.title = ""
        self.entries = []
        self.read(file)
        if entres is not None:
            self.entries = entres

    def read(self, file: str = "vide.txt"):
        """
        @summary lit un file pour redéfinir les entrés et le titre
        @param file: str -> file avec les entrés du menu
        """
        f = open(file, "r")
        content = f.read()
        data = content.split("\n")
        self.title = data[0]
        self.entries = data[1:]

    def print(self, counter=0) -> None:
        """
        @summary affiche le menu
        @param counter: int -> position du curseur si 0 affiche le nom du menu affiché
        """
        self.ecran.clear_scr()

        if counter == 0:
            self.ecran.draw_text(self.title, 0)
            for i in range(min(self.ecran.nbLign - 1, len(self.entries))):
                elmt = self.entries[(counter + i) % len(self.entries)]
                if i + 1 == self.ecran.nbLign // 2:
                    self.ecran.draw_text(str(counter + 1 + i) + "> " + elmt, i + 1)
                else:
                    self.ecran.draw_text(str(counter + 1 + i) + ". " + elmt, i + 1)
        else:
            for i in range(min(self.ecran.nbLign, len(self.entries))):
                elmt = self.entries[(counter + i - 1) % len(self.entries)]
                if i == self.ecran.nbLign // 2:
                    self.ecran.draw_text(str(counter + 1 + i) + "> " + elmt, 1)
                else:
                    self.ecran.draw_text(str(counter + 1 + i) + ". " + elmt, i)
        self.ecran.display()

    def select(self) -> int:
        """
        @summary lit l'état des boutons jusqu'a ce que OK ou BACK soit préssé
        @return  -1 si BACK
        @return  numéro de l'entré si OK 
        """
        self.print()
        self.boutons.while_pressed("OK", 3000)
        counter = 0

        while True:
            if not self.boutons.getStatus("DOWN"):
                counter += 1
                counter %= len(self.entries)
                self.print(counter)
                self.boutons.while_pressed("DOWN", 400)

            elif not self.boutons.getStatus("UP"):
                counter -= 1
                if counter < 0:
                    counter = len(self.entries)-1
                self.print(counter)
                self.boutons.while_pressed("UP", 400)


            elif not self.boutons.getStatus("OK"):
                return counter
            elif not self.boutons.getStatus("BACK"):
                return -1
