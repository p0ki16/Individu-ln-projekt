import pygame
class Shop:
    def __init__(self,thing,cost,image,button_x,button_y):
        self.active =False
        self.bought= False
        self.cost =cost
        self.image =image
        self.button_placement=button_play.get_rect(topleft=(button_x,button_y))
        self.thing =thing#1-letadlo|2raketa|3upgrdes
        
    def draw(self, screen):
        screen.blit(image,self.button_placement)
        
    def choose (self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.button_placement.collidepoint(event.pos) and self.active ==False:
            self.active = True
            
                    
      
    
        
    def buy(self,event,money):
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_placement.collidepoint(event.pos):
                
                
        
    def draw(self, screen):
        screen.blit(image,self.button_placement)
        
        
        
    