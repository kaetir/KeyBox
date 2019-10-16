import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import os

import time
import RPi.GPIO as GPIO

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 
os.system("sudo rmmod spi_bcm2835 && sudo modprobe spi_bcm2835")
time.sleep(2)

pinBtn=18
pinBtn2=17
pinBtn3=27
pinBtn4=22
pinBtn5=20

       
disp = Adafruit_SSD1306.SSD1306_128_64(rst=24, dc=23, spi=SPI.SpiDev(0, 0, max_speed_hz=8000000))
 
disp.begin()
disp.clear()
disp.display()
 
image = Image.new('1', (disp.width, disp.height))
 
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,disp.width-1,disp.height-1), outline=1, fill=0)
 
font = ImageFont.load_default()
draw.text((16, 24),'PUTE',  font=font, fill=255)

disp.image(image)
disp.display()

GPIO.setmode(GPIO.BCM)

#GPIO.cleanup()
GPIO.setup(pinBtn , GPIO.IN)
GPIO.setup(pinBtn2, GPIO.IN)
GPIO.setup(pinBtn3 , GPIO.IN)
GPIO.setup(pinBtn4, GPIO.IN)
GPIO.setup(pinBtn5, GPIO.IN)

while(True):
    etat=GPIO.input(pinBtn)
    etat2=GPIO.input(pinBtn2)
    etat3=GPIO.input(pinBtn3)
    etat4=GPIO.input(pinBtn4)
    etat5=GPIO.input(pinBtn5)
    if(etat==1 or etat2==1 or etat3==1 or etat4==1 or etat5==1):
        print("Appui detecte : " + str(etat) + " : " + str(etat2) +" : " + str(etat3) + " : " + str(etat4)+ " : " + str(etat5))
        disp.clear()
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,disp.width-1,disp.height-1), outline=1, fill=0)
        draw.text((16, 24),'bouton1 : '+str(etat),  font=font, fill=255)
        draw.text((16, 32),'bouton2 : '+str(etat2),  font=font, fill=255)
        disp.image(image)
        disp.display()


    #print(etat)
    while(etat == 1 or etat2==1 or etat3==1 or etat4==1 or etat5==1):
        time.sleep(0.1)
        etat=GPIO.input(pinBtn)
        etat2=GPIO.input(pinBtn2)
        etat3=GPIO.input(pinBtn3)
        etat4=GPIO.input(pinBtn4)
        etat5=GPIO.input(pinBtn5)



#GPIO.cleanup()

