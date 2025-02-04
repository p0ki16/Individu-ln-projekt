import pygame
import math

class Strela:
    def __init__ (self, strela_x, strela_y, angle_kanon,zasazeni):
        self.strela_x = strela_x
        self.strela_y = strela_y
        self.angle_kanon = angle_kanon
        self.zasazeni =zasazeni
        self.spawn = 20  # Přidání atributu spawn jako atribut instance
        
    def move(self,pohyb_země):
        if self.strela_y > 1080 - 20:  # 20 ke velikost výbuchu
            self.strela_y = 1080
            self.spawn -= 1  # Použití atributu instance
            self.strela_x -=pohyb_země
            
        elif self.zasazeni ==True:
            self.spawn -= 1  # Použití atributu instance
            self.strela_x -=pohyb_země
            
        else:
            self.strela_x -= 20 * math.cos(math.radians(self.angle_kanon+180))
            self.strela_y += 20 * math.sin(math.radians(self.angle_kanon+180))
            self.spawn = 20  # Použití atributu instance
    
    def draw(self, surface, image_strela, image_vybuch,vybuch):
        if self.spawn > 0:  # Použití atributu instance
            if self.strela_y > 1080 - 20:
                surface.blit(image_vybuch, (self.strela_x, self.strela_y -40))
                
            if self.zasazeni ==True:
                surface.blit(vybuch, (self.strela_x, self.strela_y))
                
            else:
                surface.blit(image_strela, (self.strela_x, self.strela_y))
                
    def zasah(self, nepritel):
        if nepritel.poloha_x < self.strela_x < nepritel.poloha_x + 150 and \
           nepritel.poloha_y < self.strela_y < nepritel.poloha_y + 200:  # hitbox
            nepritel.zivoty_self -= 1
            self.zasazeni = True

           
