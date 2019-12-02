from boutons import Boutons
from ecran import Ecran


class Menu():

    def __init__(self, ecran, boutons) -> None:
        super().__init__()
        self.ecran = ecran
        self.boutons = boutons

    def print(self):
        f = open("fichier.txt", "r")
        content = f.read()
        data = content.split("\n")
        self.ecran.draw_text(data[0], 0)
        for i in range(len(data) - 1):
            self.ecran.draw_text(str(i) + ". " + data[i + 1], i + 1)



