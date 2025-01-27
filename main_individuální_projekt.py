import pygame
import sys
from letadlo import Letadlo

clock = pygame.time.Clock()
stihacka = pygame.image.load("stíhačka_do_hry.png")
Pohyblive_pozadi = pygame.image.load("Pozadí_pohyblivé.png")
pohyb_pozadí = 0
rozdil_pozadi = 1920
výška, šířka = 1080, 1920
hrac_x = šířka * 1 / 9
hrac_y = výška / 2
zivot = 5
uhel=0
# Vytvoření instance třídy Letadlo
letadlo = Letadlo(hrac_x, hrac_y, šířka, výška,zivot,uhel)

obrazovka = pygame.display.set_mode((šířka, výška))
pygame.display.set_caption("zkouška")
pozadi_barva = (0, 255, 255)

while True:
    pohyb_pozadí -= 50
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
    
    obrazovka.fill(pozadi_barva)
    obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi1, výška - 100))  # vyobrazení pozadí
    obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi2, výška - 100))
    
    otočená_stíhačka = pygame.transform.rotate(stihacka, letadlo.uhel)
    
    obrazovka.blit(stihacka, (letadlo.x, letadlo.y))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
