import time
import RPi.GPIO as GPIO

class Boutons:
    # pin GPIO
    pinBtn=[16,19,26,21,20,27]

    # place des bouton dans le tableau pinBtn
    mapping = {
        "DOWN" : 0,
        "LEFT" : 1,
        "UP" : 2,
        "RIGHT" : 3,
        "OK" : 4,
        "BACK" : 5
    }

    def __init__(self):
        """
        @summary constructeur 
        """
        GPIO.setmode(GPIO.BCM)
        for i in self.pinBtn:
            GPIO.setup(self.pinBtn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.getState()

    def getState(self):
        """
        @summary lit l'état des boutons et le stock dans la variable status
        """
        self.status = [GPIO.input(pin) for pin in self.pinBtn]

    def getStatus(self, bouton: str):
        """
        @summary lit l'état d'un bouton par son string
        @param bouton: str -> string du nom du bouton cf var mapping
        """ 
        self.getState()
        if bouton in self.mapping:
            return self.status[self.mapping[bouton]]
        else:
            print("bad index")

    def while_pressed(self, button: str, timeout: int=500):
        """
        @summary bloque tant que le bouton est pressé ou que le timeout n'est pas passé
        @param bouton: str -> string du nom du bouton cf var mapping
        @param timeout: int -> milisecondes avant de reconsidéré un appui
        """
        t0 = int(time.time_ns())
        while int(time.time_ns()) < int(t0 + 1000000*timeout):
            self.getState()
            if self.status[self.mapping[button]]:
                return
    
    def test_mapping(self):
        """
        @summary permet de verifier le dictionnaire mapping 
        """
        while True:
            for b in self.mapping:
                print("{} : {}\t".format(b, self.getStatus(b)) , end='')
            print()
            
            
if __name__ == "__main__":
    
    mesBoutons = Boutons()
    mesBoutons.test_mapping()
            
            
            