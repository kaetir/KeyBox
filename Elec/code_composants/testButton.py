import time 
import RPi.GPIO as GPIO

pinBtn=17
pinBtn2=18

GPIO.setmode(GPIO.BCM)

#GPIO.cleanup()
GPIO.setup(pinBtn , GPIO.IN)
GPIO.setup(pinBtn2, GPIO.IN)

while(True):
    etat=GPIO.input(pinBtn)
    etat2=GPIO.input(pinBtn2)
    if(etat==1 or etat2==1):
        print("Appui detecte : " + str(etat) + " : " + str(etat2)  )
    #print(etat)
    while(etat == 1 or etat2==1):
        time.sleep(0.1)
        etat=GPIO.input(pinBtn)
        etat2=GPIO.input(pinBtn2)

GPIO.cleanup()