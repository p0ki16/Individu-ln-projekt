import pygame
import sys
from letadlo import Letadlo
from nepritel import Nepritel

# Inicializace Pygame
pygame.init()

clock = pygame.time.Clock()
stihacka = pygame.image.load("stíhačka_do_hry_kanon.png")
Pohyblive_pozadi = pygame.image.load("Pozadí_pohyblivé.png")
kanon13 = pygame.image.load("kanon_1l3.png")

pohyb_pozadí = 0
rozdil_pozadi = 1920
výška, šířka = 1080, 1920
hrac_x = šířka * 1 / 9
hrac_y = výška / 2
zivoty = 5
uhel = 0
smrt = False

rychlost_pozadi = 10
vystrel = 1

# Vytvoření instance třídy Letadlo
letadlo = Letadlo(hrac_x, hrac_y, šířka, výška, zivoty, uhel, smrt)

# Vytvoření seznamu nepřátel
nepratele = []

# Přidání několika nepřátel do seznamu
for i in range(5):
    poloha_x = šířka + i * 200  # Rozmístění nepřátel
    poloha_y = 210 + i * 100
    nepratele.append(Nepritel(rychlost_pozadi, poloha_x, poloha_y, šířka, výška, vystrel))

obrazovka = pygame.display.set_mode((šířka, výška))
pygame.display.set_caption("zkouška")
pozadi_barva = (0, 255, 255)

while True:
    if letadlo.smrt == False:
        for nepritel in nepratele:
            nepritel.pohyb_kanonu()

    pohyb_pozadí -= 50
    umisteni_pozadi1 = pohyb_pozadí % rozdil_pozadi  # počítání a přemístění pohyblivého pozadí
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
        letadlo.zivoty -= 1

    if letadlo.zivoty <= 0:
        letadlo.znic_se()

    obrazovka.fill(pozadi_barva)
    obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi1, výška - 100))  # vyobrazení pozadí
    obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi2, výška - 100))

    # Zobrazení nepřátel
    for nepritel in nepratele:
        obrazovka.blit(kanon13, (nepritel.poloha_x, nepritel.poloha_y))

    otočená_stíhačka = pygame.transform.rotate(stihacka, letadlo.uhel)
    rect = otočená_stíhačka.get_rect(center=(letadlo.x, letadlo.y))
    obrazovka.blit(otočená_stíhačka, rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
w