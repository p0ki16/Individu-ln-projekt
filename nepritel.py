import random
from strela import Strela
import pygame
class Nepritel_zem:
    
    def __init__(self, rychlost_pozadi, poloha_x, poloha_y, šířka, výška, vystrel,zivoty_self,surface,zivoty):
        self.rychlost_pozadi = rychlost_pozadi
        self.sirka = šířka
        self.vyska = výška
        self.poloha_y = poloha_y
        self.poloha_x = poloha_x  # Oprava: Použití správné proměnné
        self.vystrel = vystrel
        self.zivoty_self = zivoty_self
        self.test = 500
        self.zivoty = zivoty
        self.odecti1 = False

    def pohyb_kanonu(self):
        self.poloha_x -= self.rychlost_pozadi
        
    def respawn(self):
        self.poloha_x += random.randint(self.sirka + 500, self.sirka + 1000)
        self.zivoty_self = 25
    
    def nabíjení(self,surface,kanon13,kanon23,kanon33,kanon43,beam3l3,kanon_destroyed):
        if self.zivoty_self >0:
            vzdalenost_pred_vystrelem = self.sirka
            vzdalenost_pred_vystrelem -= self.sirka * 1 / 5
            vzdalenost_pred_vystrelem = vzdalenost_pred_vystrelem / 3
            vzdalenost_pred_vystrelem1 = vzdalenost_pred_vystrelem + self.sirka * 1 / 5
            vzdalenost_pred_vystrelem2 = vzdalenost_pred_vystrelem * 2 + self.sirka * 1 / 5
        
            
            if self.poloha_x > vzdalenost_pred_vystrelem2:
                surface.blit(kanon13, (self.poloha_x, self.poloha_y))
                
            elif self.poloha_x > vzdalenost_pred_vystrelem1:
                surface.blit(kanon23, (self.poloha_x, self.poloha_y))
                
            elif self.poloha_x > self.sirka * 1 / 5:
                surface.blit(kanon33, (self.poloha_x, self.poloha_y))
                
            elif self.poloha_x-100 < self.sirka * 1 / 5 and self.poloha_x+400 > self.sirka * 1 / 5:
                self.test += 100
                surface.blit(beam3l3, (self.poloha_x, self.poloha_y-self.test))
                surface.blit(kanon43, (self.poloha_x, self.poloha_y))
                if self.odecti1 == False:
                    self.zivoty -= 1
                self.odecti1=True
                
            elif self.poloha_x < 0 and self.poloha_x > -50 :
                 self.test = 0
                 self.odecti1=False
            elif self.poloha_x < -200: 
                 self.respawn()
                
                    
                
                
                
        elif self.poloha_x + 200 > 0:
                if self.zivoty_self <=0:
                    surface.blit(kanon_destroyed, (self.poloha_x, self.poloha_y))
                    
                else:
                    surface.blit(kanon43, (self.poloha_x, self.poloha_y))
                
        else:
            
            self.respawn()
            self.test = 0
            self.odecti1=False
            
class Nepritel_vzduch:
    
    def __init__(self, polohax, polohay, zivoty, vzhled12, vzhled22):
        self.poloha_x = polohax
        self.poloha_y = polohay + random.randint(0, 5)
        self.zivoty_self = zivoty
        self.vzhled12 = vzhled12
        self.vzhled22 = vzhled22
        self.delay = 100
        self.pohyb1 = 0.1
        self.zmena = 0
        self.pohupovani = 0
        self.uhel = 0
        self.smrt = False 
        self.odpocet = 0
        self.strileni=False
        self.vystrel = 0
        self.kdo_vystrelil = 1
    def pohyb(self,pohyb_pozadí):
        if self.smrt == False:
            self.poloha_x -= pohyb_pozadí - 5
            self.pohupovani += self.pohyb1
            self.poloha_y += self.pohyb1
            if self.pohupovani > 10 or self.pohupovani < 0:
                self.pohyb1 *= -1
        else:
            self.poloha_x -= pohyb_pozadí
            
    def animace(self):
        self.vzhled_list = [pygame.transform.rotate(self.vzhled12,self.uhel), pygame.transform.rotate(self.vzhled22,self.uhel)]
        self.zmena -= 3
        if self.zmena > 10:
            self.animace1 = 0
        else:
            self.animace1 = 1
        if self.zmena < 0:
            self.zmena = 20
        return self.vzhled_list[self.animace1]
        
    def zjev_se(self, screen):
        
        screen.blit(self.animace(), (self.poloha_x, self.poloha_y))
        
    def znic_se(self):
        if self.zivoty_self <0:
            
            if self.poloha_y < 920:
                self.poloha_y += 3
                self.poloha_x -= 2
                if self.uhel > -20:
                    self.uhel -=0.3
            
            else:
                self.smrt = True
                
    def odpocet_do_vystrelu(self,vystrel):
        self.kdo_vystrelil =0
        if self.strileni==False:
            self.odpocet+=1
            
        if self.odpocet >30:
            self.strileni = True
            
        if self.strileni:
            self.vystrel = 0
            if self.odpocet == 3:
                self.vystrel = 1
                self.odpocet -=3
            if self.odpocet == 6:
                self.vystrel = 1
                self.odpocet -=3
            if self.odpocet == 9:
                self.vystrel = 1
                self.odpocet -=3
            self.odpocet -=1
            self.kdo_vystrelil =2
        else:
            self.vystrel = 0

            
        if self.odpocet < 0:
            self.strileni = False
        
    
    
        
        
    