import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import os

import string

import time
import RPi.GPIO as GPIO

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 
pinBtn=[16,19,26,21,20,27]



GPIO.setmode(GPIO.BCM)

#boutons
for i in pinBtn:
    GPIO.setup(pinBtn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

disp = Adafruit_SSD1306.SSD1306_128_32(rst=24) 
font = ImageFont.load_default()

nbCols = 21
nbLign = 3

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
    global image
    global draw
    image = Image.new('1', (disp.width, disp.height))
    draw= ImageDraw.Draw(image) 
    disp.clear()
    disp.display()

def Menu():
    f= open("file.txt","r")
    content = f.read()
    data = content.split("\n")
    draw_text(data[0],0)
    for i in range(len(data)-1):
        draw_text(str(i)+". "+ data[i+1],i+1)
    
    
def curs(x,y):
    # x et y sont en colones lignes
    draw.rectangle((colones[x],lignes[y],colones[x]+6,lignes[y]+8), outline=1, fill=255)
    disp.image(image)
    disp.display()

Menu()


disp.image(image)
disp.display()

clear_scr()

#alphabet
"""for x in range(len(string.ascii_letters)):
    draw_text(string.ascii_letters[x],x//nbCols,x%nbCols)"""
    



#curs(1,0)
counter = 0

while True:
    asModif = False
    BtnRight= [GPIO.input(pinBtn[4])] #droite
    BtnLeft= [GPIO.input(pinBtn[1])] #gauche
    BtnUp=[GPIO.input(pinBtn[2])]
    BtnDown=[GPIO.input(pinBtn[3])]
    BtnOk= [GPIO.input(pinBtn[0])]
    
    if (False in BtnRight ):
        counter += 1
        asModif = True
        
    if (False in BtnLeft):
        counter -= 1
        asModif = True
        
    if (False in BtnUp):
        counter += 21
        asModif = True
        
    if (False in BtnDown):
        counter -= 21
        asModif = True
        
    #if (False in BtnOk):
        
    if asModif:
        clear_scr()
        Menu()
        draw_text(str(counter),4)
        disp.image(image)
        disp.display()
        time.sleep(0.2)
        
        
        

         
disp.image(image)
disp.display()
selectMenu()
