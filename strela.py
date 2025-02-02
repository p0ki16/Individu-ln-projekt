import pygame
import math

class Strela:
    def __init__ (self, strela_x, strela_y, angle_kanon):
        self.strela_x = strela_x
        self.strela_y = strela_y
        self.angle_kanon = angle_kanon
        self.spawn = 20  # Přidání atributu spawn jako atribut instance
        
    def move(self):
        if self.strela_y > 1080 - 20:  # 20 ke velikost výbuchu
            self.strela_y = 1080
            self.spawn -= 1  # Použití atributu instance
            self.strela_x -=10
        else:
            self.strela_x -= 20 * math.cos(math.radians(self.angle_kanon))
            self.strela_y += 20 * math.sin(math.radians(self.angle_kanon))
            self.spawn = 20  # Použití atributu instance
    
    def draw(self, surface, image_strela, image_vybuch):
        if self.spawn > 0:  # Použití atributu instance
            if self.strela_y > 1080 - 20:
                surface.blit(image_vybuch, (self.strela_x, self.strela_y -40))
            else:
                surface.blit(image_strela, (self.strela_x, self.strela_y))
