import random
from strela import Strela
class Nepritel:
    
    def __init__(self, rychlost_pozadi, poloha_x, poloha_y, šířka, výška, vystrel,zivoty_self,surface):
        self.rychlost_pozadi = rychlost_pozadi
        self.sirka = šířka
        self.vyska = výška
        self.poloha_y = poloha_y
        self.poloha_x = poloha_x  # Oprava: Použití správné proměnné
        self.vystrel = vystrel
        self.zivoty_self = zivoty_self 

    def pohyb_kanonu(self):
        self.poloha_x -= self.rychlost_pozadi
        
    def respawn(self):
        self.poloha_x += random.randint(self.sirka + 500, self.sirka + 1000)
    
    def nabíjení(self,surface,kanon13,kanon23,kanon33,kanon43,beam3l3):
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
            
        elif self.poloha_x-100 < self.sirka * 1 / 5 and self.poloha_x+200 > self.sirka * 1 / 5:
            surface.blit(beam3l3, (self.poloha_x, self.poloha_y-1000))
            surface.blit(kanon43, (self.poloha_x, self.poloha_y))
            
            
            
        elif self.poloha_x + 200 > 0:
            surface.blit(kanon43, (self.poloha_x, self.poloha_y))
            
        else:
            surface.blit(kanon43, (self.poloha_x, self.poloha_y))
            self.respawn()
            
    def beam_on(self,surface,beam1l3,beam2l3,beam3l3):
         surface.blit(beam3l3, (self.poloha_x, self.poloha_y))
        