import pygame
class Shop:
    def __init__(self,main_buttony,image):
        
        self.main_buttony = main_buttony
        self.image=image
        self.option1 = self.main_buttony["f_button"]
        self.option2 = self.main_buttony["myg_button"]
        self.option3 = self.main_buttony["fockerfox_button"]
        self.letadla=1
        self.letadlo = 0
        self.zmena =0
        self.moznost = 1
        self.shop = True
        self.lobby = False
        self.shown = 0
        self.obrazky_letadel =[self.main_buttony["fockerfox"],self.main_buttony["myg25"],self.main_buttony["F23"]]
        self.value_zmenena=False
        
        
    def draw_shop(self,screen):
        
        screen.blit(self.image,(0,0))
        screen.blit(self.main_buttony["letadla"],self.main_buttony["pozice_letadla"])
        screen.blit(self.main_buttony["rakety"],self.main_buttony["pozice_rakety"])
        screen.blit(self.main_buttony["upgrady"],self.main_buttony["pozice_upgrady"])
        
        
    def choose(self,event,screen):
        
        self.mouse_pos = pygame.mouse.get_pos()
        
        
        if self.moznost == 1 :
            if self.main_buttony["pozice_buttonu1"].collidepoint(self.mouse_pos) or self.letadla == 0 and self.value_zmenena==False :
                self.value_zmenena=True
                self.shown = 0 
                
                
            elif self.main_buttony["pozice_buttonu2"].collidepoint(self.mouse_pos) or self.letadla == 1 and self.value_zmenena==False :
                self.value_zmenena=True
                self.shown = 1
        
                    
            elif self.main_buttony["pozice_buttonu3"].collidepoint(self.mouse_pos) or self.letadla == 2 and self.value_zmenena==False:
                self.value_zmenena=True
                self.shown = 2
                
            if self.value_zmenena== False:
                screen.blit(self.obrazky_letadel[self.shown],self.main_buttony["pozice_modelů"])
            else:
                screen.blit(self.obrazky_letadel[self.letadla],self.main_buttony["pozice_modelů"])
                self.value_zmenena = False
                
            
            
                
        
            
        
            
        
        
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if self.main_buttony["pozice_letadla"].collidepoint(event.pos):
                self.option1 = self.main_buttony["f_button"]
                self.option2 = self.main_buttony["myg_button"]
                self.option3 = self.main_buttony["fockerfox_button"]
                self.moznost = 1
                
                
            if self.main_buttony["pozice_buttonu1"].collidepoint(event.pos) and self.moznost == 1:                
                self.letadla = 2
                
            if self.main_buttony["pozice_buttonu2"].collidepoint(event.pos) and self.moznost == 1:
                self.letadla = 1            
                
            if self.main_buttony["pozice_buttonu3"].collidepoint(event.pos) and self.moznost == 1:
                self.letadla = 0
               
                
            if self.main_buttony["pozice_rakety"].collidepoint(event.pos):
                self.option1 = self.main_buttony["f_button"]
                self.option2 = self.main_buttony["myg_button"]
                self.option3 = self.main_buttony["fockerfox_button"]
                self.moznost = 2
                
               
            if self.main_buttony["pozice_upgrady"].collidepoint(event.pos):
                self.option1 = self.main_buttony["f_button"]
                self.option2 = self.main_buttony["myg_button"]
                self.option3 = self.main_buttony["fockerfox_button"]
                self.moznost = 3
         
                
        screen.blit(self.option1,self.main_buttony["pozice_buttonu1"])
        screen.blit(self.option2,self.main_buttony["pozice_buttonu2"])
        screen.blit(self.option3,self.main_buttony["pozice_buttonu3"])
                
    def animace(self,fockerfox,f,myg):
        
        self.list_animací = [fockerfox,myg,f]
        
        self.zmena -=3
        
        if self.zmena>10:
            self.animace1=0
        else:
            self.animace1=1
        if self.zmena <0:
            self.zmena =20
         
            
            
        self.letadlo = self.list_animací[self.letadla][self.animace1]
        
    def opustit_shop(self,screen,back_button,event):
        
        self.pozice_back = back_button.get_rect(topleft=(1000, 1000))
        screen.blit(back_button,self.pozice_back)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if self.pozice_back.collidepoint(event.pos):
                self.shop=False
                self.lobby=True
                
            else:
                self.shop = True
                self.lobby = False
            
                
        
            
                    
      
