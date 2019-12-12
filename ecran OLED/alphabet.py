from boutons import Boutons
from ecran import Ecran
from menu import Menu
import string


class Alphabet(Menu):

    def __init__(self, ecran: Ecran, boutons: Boutons, file: str = "vide.txt") -> None:
        super().__init__(ecran, boutons, file)
        self.saisie = ""
        self.my_alphabet = ["valider"] + list(string.printable.replace(string.whitespace, ""))

    def disp_alphabet(self, counter_alphabet: int = 0) -> None:
        """
        @summary affiche l'alphabet
        @param counter_alphabet: int
        """
        self.ecran.clear_scr()
        elements = 0 # le nombre d'élements
        tmp = - len(self.my_alphabet[counter_alphabet % len(self.my_alphabet)]) // 2 + 1 # pos en x pour affichage

        # On affiche ce qu'il y a apres le curseur
        while tmp < self.ecran.nbCols // 2:
            elm = self.my_alphabet[(counter_alphabet + elements) % len(self.my_alphabet)]
            self.ecran.draw_text(elm, 0, self.ecran.nbCols // 2 + tmp)
            tmp += 1 + len(elm)
            elements += 1

        # on affiche ce qu'il y a avant le curseur
        tmp = -len(self.my_alphabet[counter_alphabet % len(self.my_alphabet)]) // 2 +1
        elements = -1
        while tmp > -self.ecran.nbCols // 2 +1:
            elm = self.my_alphabet[(counter_alphabet + elements) % len(self.my_alphabet)]
            tmp -= 1 + len(elm)
            # on évite le dépassement
            while self.ecran.nbCols // 2 + tmp < 0:
                elm = elm[1:]
                tmp += 1
            self.ecran.draw_text(elm, 0, self.ecran.nbCols // 2 + tmp)
            elements -= 1

        self.ecran.draw_text("^", 1, (self.ecran.nbCols - 1) // 2)
        self.ecran.draw_text(self.saisie, 2)

        self.ecran.display()

    def select_alphabet(self) -> None:
        """
        @summary lit l'état des boutons jusqu'a ce que counter alphabet soit 0 et que OK soit préssé
        @return  -1 si BACK
        @return  numéro de l'entré si OK
        """
        self.saisie = ""
        self.disp_alphabet()
        self.boutons.while_pressed("OK", 4000)
        counterAlphabet = 0

        while True:

            if not self.boutons.getStatus("RIGHT"):
                counterAlphabet += 1
                counterAlphabet %= len(self.my_alphabet)
                self.boutons.while_pressed("RIGHT")
                # on a appuié sur un bouton
                self.disp_alphabet(counterAlphabet)

            elif not self.boutons.getStatus("LEFT"):
                counterAlphabet -= 1
                if counterAlphabet < 0:
                    counterAlphabet = len(self.my_alphabet)-1
                self.boutons.while_pressed("LEFT")
                # on a appuié sur un bouton
                self.disp_alphabet(counterAlphabet)

            elif not self.boutons.getStatus("UP"):
                counterAlphabet += len(string.ascii_letters) // 4
                self.boutons.while_pressed("UP")
                # on a appuié sur un bouton
                self.disp_alphabet(counterAlphabet)

            elif not self.boutons.getStatus("DOWN"):
                counterAlphabet -= len(string.ascii_letters) // 4
                self.boutons.while_pressed("DOWN")
                # on a appuié sur un bouton
                self.disp_alphabet(counterAlphabet)

            elif not self.boutons.getStatus("OK"):
                if counterAlphabet == 0:
                    return self.saisie
                self.saisie += self.my_alphabet[counterAlphabet]
                self.boutons.while_pressed("OK", 1000)
                # on a appuié sur un bouton
                self.disp_alphabet(counterAlphabet)

            elif not self.boutons.getStatus("BACK"):
                self.saisie = self.saisie[:-1]
                self.boutons.while_pressed("BACK", 1000)



