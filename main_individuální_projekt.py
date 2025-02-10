# Importy a inicializace
import pygame
import sys
import random
import math

from strela import Strela,Raketa
from letadlo import Letadlo
from nepritel import Nepritel
    


pygame.font.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 48)


text_color = (0, 0, 0)



firerate = 0


# Inicializace proměnných
angle_kanon = 180
pohyb_pozadí = 0
rozdil_pozadi = 1920
výška, šířka = 1080, 1920
hrac_x = šířka * 1 / 5
hrac_y = výška / 2

zivoty = 8
zivoty_nepritel = 20
uhel = 1

smrt = False
raketa_vystrelena =0
vystrel = 0
speed_strela = 5
rychlost_pozadi = 10
poloha_x = šířka
poloha_y = výška - 210
firerate_rakety =0
vystreleni = []
raketa_vystrel =[]
pocet_raket=12
skore=0


# Inicializace Pygame
obrazovka = pygame.display.set_mode((šířka, výška))
pygame.display.set_caption("zkouška")
pozadi_barva = (100, 100, 255)

# Načtení obrázků
kanon = pygame.image.load('kanon_stíhačka.png').convert_alpha()
kanon_rect = kanon.get_rect()
Raketa_image = pygame.image.load('Raketa.png')

stihacka = pygame.image.load("stíhačka_kanon_moderní.png")
Pohyblive_pozadi = pygame.image.load("Pozadí_pohyblivé.png")

kanon13 = pygame.image.load("kanon_1l3.png")
kanon23 = pygame.image.load("kanon_2l3.png")
kanon33 = pygame.image.load("kanon_3l3.png")
kanon43 = pygame.image.load("kanon_4l3.png")

kanon_destroyed = pygame.image.load("kanon_destroyed.png")

strela_image = pygame.image.load("strela.png")
vybuch_image = pygame.image.load("výbuch_strely.png")

beam3l3 = pygame.image.load("beam.png")
vybuch = pygame.image.load("výbuch.png")

Lobby_image = pygame.image.load("Lobby.png")

button_play = pygame.image.load("button_play.png")  
pozice_play = button_play.get_rect(topleft=(600, 100))

button_shop = pygame.image.load("button_shop.png")  
pozice_shop= button_shop.get_rect(topleft=(600, 200))

button_infinity = pygame.image.load("button_infinity.png")  
pozice_infinity = button_infinity.get_rect(topleft=(600, 300))

shop_image = pygame.image.load("Shop.png")



Lobby = True
Infinite_mode = False 
shop = False 


# Vytvoření instancí tříd
letadlo = Letadlo(hrac_x, hrac_y, šířka, výška, zivoty, uhel, smrt, 0, 0, vystrel, angle_kanon)
nepritel = Nepritel(rychlost_pozadi, poloha_x, poloha_y, šířka, výška, vystrel, zivoty_nepritel, obrazovka, zivoty)
while True:
    
    while Lobby:
        
        for udalost in pygame.event.get():
            
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if udalost.type == pygame.MOUSEBUTTONDOWN:
                
                if pozice_play.collidepoint(udalost.pos):  # Kontrola, zda kliknutí bylo na obrázku tlačítka
                    Lobby = False
                    play=True
                    
                if pozice_shop.collidepoint(udalost.pos):  # Kontrola, zda kliknutí bylo na obrázku tlačítka
                    Lobby = False
                    shop = True
                    
                if pozice_infinity.collidepoint(udalost.pos):  # Kontrola, zda kliknutí bylo na obrázku tlačítka
                    Lobby = False
                    Infinite_mode = True
                    
        umisteni_pozadi1 = pohyb_pozadí % rozdil_pozadi
        umisteni_pozadi2 = (pohyb_pozadí % rozdil_pozadi) - rozdil_pozadi
        
         # Vypočítej ofset od středu obrázku k pravému hornímu rohu
        
        
        
        
        
        # Poté vyplníme pozadí
        obrazovka.fill(pozadi_barva)
        obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi1, výška - 100))
        obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi2, výška - 100))
        
        # Vykreslíme ostatní obrázky (např. pozadí Lobby)
        obrazovka.blit(Lobby_image, (-20, 0))
        # Nejprve vykreslíme tlačítka
        obrazovka.blit(button_play, pozice_play)
        obrazovka.blit(button_shop, pozice_shop)
        obrazovka.blit(button_infinity, pozice_infinity)

        # Aktualizace obrazovky
        pygame.display.flip()
        
        # Nastavení FPS
        clock.tick(60)
        
    while shop:
        
        for udalost in pygame.event.get():
    
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        obrazovka.blit(shop_image, (0,0))
        pygame.display.flip()
        
        # Nastavení FPS
        clock.tick(60)
    
            
        
        
        

        
    while Infinite_mode:
        
        text = f" skóre: {skore} počet raket :{pocet_raket} životy:{nepritel.zivoty} "
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(500, 50))
        
        
        for i in range(vystrel):
            strela_x = letadlo.x + 17
            strela_y = letadlo.y + 17
            zasazeni = False
            strela = Strela(strela_x, strela_y, letadlo.uhel, zasazeni)
            vystreleni.append(strela)
            
        for j in range(raketa_vystrelena):
            Raketa_x = letadlo.x
            Raketa_y = letadlo.y
            zasazeni = False
            raketa = Raketa(Raketa_x, Raketa_y, zasazeni)
            raketa_vystrel.append(raketa)
            
            
        for udalost in pygame.event.get():
                if udalost.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        if letadlo.y > 1080:
            nepritel.zivoty=0
          
        
        if nepritel.zivoty <= 0:
                letadlo.znic_se()
        else:       
        
            
            
           
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                letadlo.pohyb_dolu()
        
            letadlo.pohyb_jiným_směrem()
            
            if firerate > 0:  # Delay mezi střelami
                firerate -= 1
                
            if firerate_rakety > 0:  # Delay mezi raketami
                firerate_rakety -= 1
                
            vystrel = 0    
            if keys[pygame.K_SPACE] and firerate == 0:
                firerate = 0  # Nastavení hodnoty delay
                vystrel = 1
                
            raketa_vystrelena = 0
            
            if keys[pygame.K_LALT] and firerate_rakety == 0 and pocet_raket>0:
                firerate_rakety = 100  # Nastavení hodnoty delay
                raketa_vystrelena = 1
                pocet_raket-=1
            
            if keys[pygame.K_UP]:
                letadlo.pohyb_nahoru()
            nepritel.rychlost_pozadi =6   #počítání pohybu pod úhlem
            
            if 270>letadlo.uhel and letadlo.uhel  < 90:   
                nepritel.rychlost_pozadi =-nepritel.rychlost_pozadi * math.sin(math.radians(letadlo.uhel-90))#90je zde k pootočení osy
                
            else:
                nepritel.rychlost_pozadi =-nepritel.rychlost_pozadi * math.sin(math.radians(letadlo.uhel-90))
                
            
        
        
            
            
        if letadlo.smrt == False:  # Kontrola jestli letadlo žije
            nepritel.pohyb_kanonu()
            pohyb_pozadí -= nepritel.rychlost_pozadi
            umisteni_pozadi1 = pohyb_pozadí % rozdil_pozadi
            umisteni_pozadi2 = (pohyb_pozadí % rozdil_pozadi) - rozdil_pozadi
        
            
        
       

        obrazovka.fill(pozadi_barva)
        obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi1, výška - 100))
        obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi2, výška - 100))
        
        nepritel.nabíjení(obrazovka, kanon13, kanon23, kanon33 , kanon43, beam3l3,kanon_destroyed)
       
        for strela in vystreleni:
            
            if strela.zasazeni == False :
                
                strela.zasah(nepritel)
            strela.move( pohyb_pozadí)
            strela.draw(obrazovka, strela_image, vybuch_image,vybuch)
            
        for raketa in raketa_vystrel:
            
            if raketa.zasazeni == False:
                raketa.zasah(nepritel)
            raketa.navádění(nepritel,obrazovka,Raketa_image,výška,nepritel.rychlost_pozadi)
            raketa.draw(obrazovka, Raketa_image, vybuch_image,vybuch, nepritel.rychlost_pozadi)
            
        if nepritel.zivoty_self > 0:
            pricteni =True
            
        if nepritel.zivoty_self < 0 and pricteni ==True:
            skore+=1000
            pricteni =False
    
                
            
                
        

        otočená_stíhačka = pygame.transform.rotate(stihacka, letadlo.uhel)
        

        rect = otočená_stíhačka.get_rect(center=(letadlo.x, letadlo.y))
        obrazovka.blit(otočená_stíhačka, rect.topleft)
        obrazovka.blit(text_surface, text_rect)
        print(letadlo.y)
        letadlo.neutíkej()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
