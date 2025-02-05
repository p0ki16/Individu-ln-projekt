import pygame
class Shop:
    def __init__(self,active,cost,image,button_x,button_y):
        self.active =active
        self.cost =cost
        self.image =image
        self.button_placement=button_play.get_rect(topleft=(button_x,button_y))
    def choose (self)    
    def buy(self,event,money):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_placement.collidepoint(event.pos):
                if self.active == 1:
                    money-=cost
                    self.active =3
                elif self.active == 3:#3=equip|2=vlastněno ale neequipd|1= nevlastněno
                    self.active == 2
                else:
                    self.active =3
        
        
    def draw(self, screen):
        screen.blit(image,self.button_placement)
        
        
        
    