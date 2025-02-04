# Importy a inicializace
import pygame
import sys
import random
import math

from strela import Strela
from letadlo import Letadlo
from nepritel import Nepritel

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 48)


firerate = 0


# Inicializace proměnných
angle_kanon = 180
pohyb_pozadí = 0
rozdil_pozadi = 1920
výška, šířka = 1080, 1920
hrac_x = šířka * 1 / 5
hrac_y = výška / 2

zivoty = 1
zivoty_nepritel = 10
uhel = 0

smrt = False

vystrel = 0
speed_strela = 5
rychlost_pozadi = 10
poloha_x = šířka
poloha_y = výška - 210

vystreleni = []

# Inicializace Pygame
obrazovka = pygame.display.set_mode((šířka, výška))
pygame.display.set_caption("zkouška")
pozadi_barva = (100, 100, 255)

# Načtení obrázků
kanon = pygame.image.load('kanon_stíhačka.png').convert_alpha()
kanon_rect = kanon.get_rect()

stihacka = pygame.image.load("stíhačka_do_hry_kanon.png")
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
pozice_play = button_play.get_rect(topright=(200, 150))

button_levels = pygame.image.load("button_levels.png")  
pozice_levels = button_levels.get_rect(topleft=(200, 250))

button_infinity = pygame.image.load("button_infinity.png")  
pozice_infinity = button_infinity.get_rect(topleft=(200, 350))

Lobby=True
Infinite_mode=True 

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
                    print("Tlačítko 'Play' bylo kliknuto!")
                if pozice_levels.collidepoint(udalost.pos):  # Kontrola, zda kliknutí bylo na obrázku tlačítka
                    print("Tlačítko 'Levels' bylo kliknuto!")
                if pozice_infinity.collidepoint(udalost.pos):  # Kontrola, zda kliknutí bylo na obrázku tlačítka
                    Lobby = False
                    Infinite_mode = True
                    print("Přechod na Infinite Mode!")

        # Nejprve vykreslíme tlačítka
        obrazovka.blit(button_play, pozice_play)
        obrazovka.blit(button_levels, pozice_levels)
        obrazovka.blit(button_infinity, pozice_infinity)
        
        # Poté vyplníme pozadí
        obrazovka.fill(pozadi_barva)
        
        # Vykreslíme ostatní obrázky (např. pozadí Lobby)
        obrazovka.blit(Lobby_image, (-20, 0))

        # Aktualizace obrazovky
        pygame.display.flip()
        
        # Nastavení FPS
        clock.tick(60)

        
    while Infinite_mode:
        for i in range(vystrel):
            strela_x = letadlo.x + 17
            strela_y = letadlo.y + 17
            zasazeni = False
            strela = Strela(strela_x, strela_y, letadlo.angle_kanon, zasazeni)
            vystreleni.append(strela)
            
        for udalost in pygame.event.get():
                if udalost.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
        if nepritel.zivoty <= 0:
                letadlo.znic_se()
        else:       
        
            
            
           
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                letadlo.pohyb_dolu()
                
            vystrel = 0
            if firerate > 0:  # Delay mezi střelami
                firerate -= 1
                
            if keys[pygame.K_SPACE] and firerate == 0:
                firerate = 10  # Nastavení hodnoty delay
                vystrel = 1
            
            if keys[pygame.K_UP]:
                letadlo.pohyb_nahoru()
                
            if keys[pygame.K_RIGHT] or keys[pygame.K_w]:
                if not letadlo.angle_kanon > 180:
                    letadlo.angle_kanon += 1
                    
            if keys[pygame.K_LEFT] or keys[pygame.K_s]:
                if not letadlo.angle_kanon < 60:
                    letadlo.angle_kanon -= 1
        if letadlo.smrt == False:  # Kontrola jestli letadlo žije
            nepritel.pohyb_kanonu()
            pohyb_pozadí -= nepritel.rychlost_pozadi             
        

        umisteni_pozadi1 = pohyb_pozadí % rozdil_pozadi
        umisteni_pozadi2 = (pohyb_pozadí % rozdil_pozadi) - rozdil_pozadi

        # Vypočítej ofset od středu obrázku k pravému hornímu rohu
        image_center = pygame.math.Vector2(kanon_rect.center)
        pivot = pygame.math.Vector2(kanon_rect.midright)
        offset = pivot - image_center

        # Otoč ofset
        rotated_offset = offset.rotate(-letadlo.angle_kanon)

        # Otoč obrázek
        rotated_image = pygame.transform.rotate(kanon, letadlo.angle_kanon)
        rotated_rect = rotated_image.get_rect()

        # Nastav novou pozici obrázku
        new_center = pygame.math.Vector2(letadlo.x + 30, letadlo.y + 20) - rotated_offset
        rotated_rect.center = new_center

        obrazovka.fill(pozadi_barva)
        obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi1, výška - 100))
        obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi2, výška - 100))
        
        nepritel.nabíjení(obrazovka, kanon13, kanon23, kanon33, kanon43, beam3l3,kanon_destroyed)
       
        for strela in vystreleni:
            if strela.zasazeni == False :
                strela.zasah(nepritel)
            strela.move()
            strela.draw(obrazovka, strela_image, vybuch_image,vybuch)
                
                
            
                
            # Kontrola hodnoty zivoty nepritel

        otočená_stíhačka = pygame.transform.rotate(stihacka, letadlo.uhel)
        obrazovka.blit(rotated_image, rotated_rect)

        rect = otočená_stíhačka.get_rect(center=(letadlo.x, letadlo.y))
        obrazovka.blit(otočená_stíhačka, rect.topleft)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
