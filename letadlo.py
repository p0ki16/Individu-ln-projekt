import math
class Letadlo:
    def __init__(self, hrac_x, hrac_y, šířka, výška, zivoty, uhel,smrt,strela_x,strela_y,vystrel,angle_kanon):
        self.sirka = šířka
        self.vyska = výška
        self.x = hrac_x if hrac_x is not None else šířka * 1 / 4
        self.y = hrac_y if hrac_y is not None else výška / 2
        self.zivoty = zivoty
        self.uhel = uhel
        self.angle_kanon = angle_kanon
        self.DOWN = 0
        self.UP = 0
        self.smrt = False

    def pohyb_dolu(self):
        
        self.uhel -=3
        
            
    def pohyb_nahoru(self):
        
        self.uhel +=3
        
    def pohyb_jiným_směrem(self):
        if self.uhel < 180:
            self.y -= 25 * abs(math.sin(math.radians(self.uhel)))
        else:
            self.y += 25 * abs(math.sin(math.radians(self.uhel)))
            
        if self.uhel < 0:
            self.uhel =360
        if self.uhel > 360:
            self.uhel =0
        
        
            
    def znic_se(self):
        if self.y <self.vyska-20:
            self.y += 10
            if self.uhel > -50:
                self.uhel -=1
        else:
            self.smrt = True
            
    def neutíkej(self):
        if self.y < -500:
            self.uhel = 360-self.uhel
    
            
    
     

                
    