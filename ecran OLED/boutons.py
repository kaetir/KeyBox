
import RPi.GPIO as GPIO

class Boutons:
    # pin GPIO
    pinBtn=[16,19,26,21,20,27]

    # place des bouton dans le tableau pinBtn
    mapping = {
        "DOWN" : 0,
        "UP" : 1,
        "LEFT" : 2,
        "RIGHT" : 3,
        "OK" : 4,
        "BACK" : 5
    }

    status = []

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        for i in self.pinBtn:
            GPIO.setup(self.pinBtn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def getState(self):
        self.status = [GPIO.input(pin) for pin in self.pinBtn]

    def getStatus(self, bouton):
        self.getState()
        if bouton in self.mapping:
            return self.status[self.mapping[bouton]]

