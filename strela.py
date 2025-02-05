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
class Raketa:
    def __init__ (self,raketa_x,raketa_y,zasazeni):
        self.raketa_x =raketa_x
        self.raketa_y =raketa_y
        self.zasazeni =zasazeni
        self.délka_navádění =1000
    
    def navádění(self,nepritel,screen,raketa,výška):
        
        
        if self.délka_navádění>0:
            self.délka_navádění-=1
        else:
            self.raketa_y=výška +100
            
        
        # Výpočet rozdílu v pozicích
        dx = nepritel.poloha_x - self.raketa_x
        dy = nepritel.poloha_y - self.raketa_y
        
        # Výpočet vzdálenosti mezi kuličkou a kurzorem
        distance = math.sqrt(dx**2 + dy**2)
        
        # Normování směrového vektoru
        if distance != 0:
            dx /= distance
            dy /= distance
        
        # Aktualizace pozice kuličky
        self.raketa_x += dx * 2
        self.raketa_y += dy * 2
        

        # Kreslení kuličky na aktuální pozici
        
        screen.blit(raketa,(int(self.raketa_x), int(self.raketa_y)))
                      
                  
                  
                  
                  
    def zasah(self, nepritel):
        if nepritel.poloha_x < self.raketa_x < nepritel.poloha_x + 150 and \
           nepritel.poloha_y < self.raketa_y < nepritel.poloha_y + 200:  # hitbox
           nepritel.zivoty_self -= 10
           self.zasazeni = True

           
