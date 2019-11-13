import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import os

import string

import time
import RPi.GPIO as GPIO

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 
os.system("sudo rmmod spi_bcm2835 && sudo modprobe spi_bcm2835")
time.sleep(2)

pinBtn=[16,19,20,21,26]


GPIO.setmode(GPIO.BCM)

disp = Adafruit_SSD1306.SSD1306_128_64(rst=24, dc=23, spi=SPI.SpiDev(0, 0, max_speed_hz=8000000))
font = ImageFont.load_default()

nbCols = 21
nbLign = 6
lignes= [ i*10 for i in range(nbLign)]
colones = [i * 6 for i in range(nbCols)]
 
disp.begin()
disp.clear()
disp.display()

image = Image.new('1', (disp.width, disp.height)) 
draw = ImageDraw.Draw(image)
    

def draw_text(text, ligne, col = 0):
    if ligne > nbLign-1 or col > nbCols - 1:
        return 
    # TODO recalcyuler avec le nouvel écran
    draw.text((colones[col]+2,lignes[ligne]),text, font=font, fill=255)

def clear_scr():
    draw = ImageDraw.Draw(image)
    disp.clear()
    disp.display()

 
def Menu():
    draw_text("Menu", 0)
    draw_text("1. G-mail", 1)
    draw_text("2. Facebook", 2)
    draw_text("3. Twitter", 3)
    draw_text("pornhub.com", 4, 3)
        
def curs(x,y):
    # x et y sont en colones lignes
    draw.rectangle((colones[x],lignes[y],colones[x]+6,lignes[y]+8), outline=1, fill=255)
    disp.image(image)
    disp.display()

#Menu()
disp.image(image)
disp.display()

clear_scr()

for x in range(len(string.ascii_letters)):
    draw_text(string.ascii_letters[x],x//nbCols,x%nbCols)
    
disp.image(image)
disp.display()

curs(1, 0)

counter = 0
x=0

for i in pinBtn:
    GPIO.setup(pinBtn, GPIO.IN, pull_up_down=GPIO.PUD_UP)


"""
while(True):
    etat= [GPIO.input(i) for i in pinBtn]

    if(False in etat):
        print("Appui detecte : "+ str(etat))
        disp.clear()
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,disp.wiBtn_Lefth-1,disp.height-1), outline=1, fill=0)
        draw.text((8,15),'ID: ANTOINE', font=font, fill=255)
        draw.text((8,25),'Password: ********', font=font, fill=255)
        
        disp.image(image)
        disp.display()"""



while True:
    BtnRight= [GPIO.input(pinBtn[4])] #droite
    BtnLeft= [GPIO.input(pinBtn[1])] #gauche
    BtnUp=[GPIO.input(pinBtn[2])]
    BtnDown=[GPIO.input(pinBtn[3])]
    if (False in BtnRight ):
        counter += 1
        time.sleep(0.2)
        print(counter)
        
    elif (False in BtnLeft):
        counter -= 1
        time.sleep(0.2)
        print (counter)
        
    elif (False in BtnUp):
        counter += 21
        time.sleep(0.2)
        print(counter)
        
    elif (False in BtnDown):
        counter -= 21
        time.sleep(0.2)
        print(counter)