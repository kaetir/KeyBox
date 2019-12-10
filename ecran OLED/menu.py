from boutons import Boutons
from ecran import Ecran
import string

class Menu():
    
    my_alphabet = string.printable.replace(string.whitespace,"")

    def __init__(self, ecran: Ecran, boutons: Boutons, fichier: str ="Comptes.txt") -> None:
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
        self.saisie = []

    def print(self, counter=0) -> None:
        """
        @summary affiche le menu
        @param counter: int -> position du curseur si 0 affiche le nom du menu affiché
        """
        self.ecran.clear_scr()
        if counter == 0:
            self.ecran.draw_text(self.title, 0)
            self.ecran.draw_text(str((counter+1)%len(self.entries)) + "> " +self.entries[counter],1 )
            self.ecran.draw_text(str(counter+2) + ". " +self.entries[counter+1],2 )
        else:
            for i in range(self.ecran.nbLign):
                elmt =  self.entries[(counter+i)%len(self.entries)]
                if i == self.ecran.nbLign // 2:
                    self.ecran.draw_text(str(counter%(len(self.entries)+1)+i) + "> " + elmt,1 )
                else:
                    self.ecran.draw_text(str(counter%(len(self.entries)+1)+i) + ". " + elmt,i )
        self.ecran.display()
        
    def alphabet(self, counterAlphabet=0) -> None:
        self.ecran.clear_scr()

        self.ecran.draw_text("v",0,(self.ecran.nbCols-1)//2)
        for i in range(self.ecran.nbCols):
            elmt =  self.my_alphabet[(counterAlphabet+i)%len(self.my_alphabet)]
            self.ecran.draw_text(elmt,1,i)
        for l in self.saisie:
            self.ecran.draw_text(l,2,self.saisie.index(l))
        
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
            if self.boutons.getStatus("DOWN")==False:
                counter+=1
                counter %= len(self.entries)
                self.print(counter)
                while self.boutons.getStatus("DOWN")==False:
                    self.boutons.getStatus("DOWN")
                
            elif self.boutons.getStatus("UP")==False:
                counter-=1
                if counter < 0:
                    counter = len(self.entries)
                self.print(counter)
                while self.boutons.getStatus("UP")==False:
                    self.boutons.getStatus("UP")
            elif self.boutons.getStatus("OK")==False :
                return counter+1
            elif self.boutons.getStatus("BACK")==False:
                return -1
        
    def selectAlphabet(self) ->None:
        self.alphabet()
        position=0
        counterAlphabet=0
        while True:
            
            if self.boutons.getStatus("RIGHT")==False:
                counterAlphabet+=1
                counterAlphabet %= len(string.ascii_letters)
                self.boutons.while_pressed("RIGHT")
                
            elif self.boutons.getStatus("LEFT")==False:
                counterAlphabet-=1
                if counterAlphabet < 0:
                   counterAlphabet = len(self.my_alphabet)
                self.boutons.while_pressed("LEFT")
                    
            elif self.boutons.getStatus("UP")==False:
                counterAlphabet+=len(string.ascii_letters)//2
                counterAlphabet %= len(string.ascii_letters)
                self.boutons.while_pressed("UP")
                    
            elif self.boutons.getStatus("DOWN")==False:
                counterAlphabet-=len(string.ascii_letters)//2
                counterAlphabet %= len(string.ascii_letters)
                self.boutons.while_pressed("DOWN")
                    
            elif self.boutons.getStatus("OK")==False:
                a=(counterAlphabet+(self.ecran.nbCols//2))%len(self.my_alphabet)
                self.saisie += self.my_alphabet[a]
                position+=1
                self.boutons.while_pressed("OK", 1500)
            
            elif self.boutons.getStatus("BACK")==False:
                self.saisie = self.saisie[:-1]
                self.boutons.while_pressed("BACK", 1500)
                
            if False in self.boutons.status :
                self.alphabet(counterAlphabet)