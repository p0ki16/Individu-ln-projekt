import pygame
import sys
from letadlo import Letadlo
from nepritel import Nepritel

clock = pygame.time.Clock()



stihacka = pygame.image.load("stíhačka_do_hry_kanon.png")
Pohyblive_pozadi = pygame.image.load("Pozadí_pohyblivé.png")
kanon13= pygame.image.load("kanon_1l3.png")
kanon23= pygame.image.load("kanon_2l3.png")
kanon33= pygame.image.load("kanon_3l3.png")
kanon43 = pygame.image.load("kanon_4l3.png")








pohyb_pozadí = 0
rozdil_pozadi = 1920
výška, šířka = 1080, 1920
hrac_x = šířka * 1 / 5
hrac_y = výška / 2
zivoty = 5
uhel=0
smrt = False




rychlost_pozadi=10
poloha_x = šířka
poloha_y = výška - 210

vystrel=1
# Vytvoření instance třídy Letadlo
letadlo = Letadlo(hrac_x, hrac_y, šířka, výška,zivoty,uhel,smrt)
nepritel = Nepritel(rychlost_pozadi,poloha_x,poloha_y,šířka, výška,vystrel)

obrazovka = pygame.display.set_mode((šířka,výška))
pygame.display.set_caption("zkouška")
pozadi_barva = (100, 100, 255)

while True:
    nepritel.nabíjení()
    
    if letadlo.smrt == False:
        nepritel.pohyb_kanonu()
        pohyb_pozadí -= nepritel.rychlost_pozadi
    umisteni_pozadi1 = pohyb_pozadí % rozdil_pozadi  # počítání a přemistování pohyblivého pozadí
    umisteni_pozadi2 = (pohyb_pozadí % rozdil_pozadi) - rozdil_pozadi
    
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        letadlo.pohyb_dolu()
        
    if keys[pygame.K_w]:
        letadlo.pohyb_nahoru()
    if keys[pygame.K_m]:
        letadlo.zivoty -=1 
        
        
    if letadlo.zivoty <= 0:
        letadlo.znic_se()
    

    
    obrazovka.fill(pozadi_barva)
    obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi1, výška - 100))  # vyobrazení pozadí
    obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi2, výška - 100))
    
    
    if nepritel.vystrel == 1: # animace nabíjení
        obrazovka.blit(kanon13,(nepritel.poloha_x,nepritel.poloha_y))
    elif nepritel.vystrel == 2:
        obrazovka.blit(kanon23,(nepritel.poloha_x,nepritel.poloha_y))
    elif nepritel.vystrel == 3 :
        obrazovka.blit(kanon33,(nepritel.poloha_x,nepritel.poloha_y))
    else:
        obrazovka.blit(kanon43,(nepritel.poloha_x,nepritel.poloha_y))
    
    
    otočená_stíhačka = pygame.transform.rotate(stihacka, letadlo.uhel)
    rect = otočená_stíhačka.get_rect(center=(letadlo.x, letadlo.y))
    obrazovka.blit(otočená_stíhačka, rect.topleft)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
