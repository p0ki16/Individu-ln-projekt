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
        self.delay = 100
        self.pocet_raket =12
        self.skore=0
        
        

    def pohyb_dolu(self,obratnost):
        
        self.uhel -=obratnost
        
            
    def pohyb_nahoru(self,obratnost):
        
        self.uhel +=obratnost
        
    def pohyb_jiným_směrem(self):
        if self.uhel < 180:
            self.y -= 15 * abs(math.sin(math.radians(self.uhel)))
        else:
            self.y += 20 * abs(math.sin(math.radians(self.uhel)))
            
        if self.uhel < 0:
            self.uhel =360
        if self.uhel > 360:
            self.uhel =0
        
        
            
    def znic_se(self,lobby,hra):
        if self.y <self.vyska-20:
            self.y += 10
            
            if self.uhel > -50:
                self.uhel -=1
        else:
            self.smrt = True
            self.delay-=1
            
            if self.delay<0:
                return True
                
            
            
    def neutíkej(self):
        if self.y < -500:
            self.uhel = 360-self.uhel
            
    def reset(self,nepritel,nepritel_vzduch):
        self.x = self.sirka * 1 / 4
        self.y = self.vyska / 2
        nepritel.zivoty = 5
        nepritel_vzduch.zivoty_self = 30
        self.smrt = False
        self.uhel =0
        nepritel_vzduch.smrt = False
        nepritel_vzduch.uhel =0
        nepritel_vzduch.poloha_x = 1920
        nepritel.poloha_x=1920
        nepritel_vzduch.poloha_y=500
        self.pocet_raket =12
        self.skore=0
        
        
class Powerup:
    def __init__(self,balicky):
       self.image_powerupu = balicky
       self.cekani_na_spawn = 1
       self.poloha_x = 0
       self.poloha_y = 0
       self.smrt = False
       self.pohyb1 = 0.1
       self.pohupovani = 0
       
    def spawn(self,surface):
        self.cekani_na_spawn +=1 
        if self.cekani_na_spawn >1000:
            self.poloha_x =1200
            self.poloha_y =0
            self.cekani_na_spawn =0
            
        if self.smrt == False:
            surface.blit(self.image_powerupu, (self.poloha_x, self.poloha_y ))
            
            
    def pohyb(self,pohyb_pozadí):
        if self.smrt == False:
            self.poloha_x -= pohyb_pozadí
            print(pohyb_pozadí)
            
        
            self.poloha_y += 1
    
                
            
    
     

                
    
    
    
    
    