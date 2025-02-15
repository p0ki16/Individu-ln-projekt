import pygame
class Shop:
    def __init__(self,main_buttony,image):
        
        self.main_buttony = main_buttony
        self.image=image
    def draw_shop(self,screen):
        screen.blit(self.image,(0,0))
        screen.blit(self.main_buttony["letadla"],self.main_buttony["pozice_letadla"])
        screen.blit(self.main_buttony["rakety"],self.main_buttony["pozice_rakety"])
        screen.blit(self.main_buttony["upgrady"],self.main_buttony["pozice_upgrady"])
        
    def choose(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if self.main_buttony["pozice_letadla"].collidepoint(event.pos):
                print(":)")
                
            if self.main_buttony["pozice_rakety"].collidepoint(event.pos):
               print(":(")
               
            if self.main_buttony["pozice_upgrady"].collidepoint(event.pos):
                print(":-)")
            
                    
      
