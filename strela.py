import pygame
import math

class Strela:
    def __init__ (self,strela_x,strela_y,angle_kanon):
        
        self.strela_x = strela_x
        self.strela_y = strela_y
        self.angle_kanon = angle_kanon
        
    def move(self):
        self.strela_x -= 20* math.cos(math.radians(self.angle_kanon))
        self.strela_y += 20 * math.sin(math.radians(self.angle_kanon))

    def draw(self, surface,image):
        surface.blit(image, (self.strela_x,self.strela_y))
    