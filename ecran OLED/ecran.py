import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 



class Ecran:
        
    nbCols = 21
    nbLign = 3
    lignes= [i*10 for i in range(nbLign)]
    colones = [i * 6 for i in range(nbCols)]

    def __init__(self):
        self.disp = Adafruit_SSD1306.SSD1306_128_32(rst=24) 
        self.disp.begin()
        self.disp.clear()
        self.disp.display()
        self.font = ImageFont.load_default()
        self.image = Image.new('1', (self.disp.width, self.disp.height))
        self.draw = ImageDraw.Draw(self.image)

    def display(self):
        self.disp.image(self.image)
        self.disp.display()


    def draw_text(self, text, ligne, col = 0):
        if ligne > self.nbLign-1 or col > self.nbCols - 1:
            return
        self.draw.text((self.colones[col]+2, self.lignes[ligne]),text,
                       font=self.font, fill=255)

    def clear_scr(self):
        self.image = Image.new('1', (self.disp.width, self.disp.height))
        self.draw= ImageDraw.Draw(self.image)
        self.disp.clear()
        self.disp.display()
    
    
    def curs(self,x,y):
        # x et y sont en colones lignes
        self.draw.rectangle((self.colones[x],self.lignes[y],self.colones[x]+6,self.lignes[y]+8), outline=1, fill=255)
        self.disp.image(self.image)

