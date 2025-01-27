import pygame
import sys

# Inicializace Pygame
pygame.init()

# Nastavení obrazovky
šířka, výška = 800, 600
obrazovka = pygame.display.set_mode((šířka, výška))
pygame.display.set_caption("Naklánění obrázku v Pygame")

# Načtení obrázku
stíhačka = pygame.image.load("stíhačka_do_hry.png")

# Výchozí úhel otočení
úhel = 0

# Hlavní smyčka hry
while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Otočení obrázku
    otočená_stíhačka = pygame.transform.rotate(stíhačka, úhel)

    # Vymazání obrazovky
    obrazovka.fill((0, 255, 255))

    # Získání nových souřadnic obrázku
    rect = otočená_stíhačka.get_rect(center=(šířka // 2, výška // 2))

    # Zobrazení otočeného obrázku
    obrazovka.blit(otočená_stíhačka, rect.topleft)

    # Aktualizace obrazovky
    pygame.display.flip()

    # Zvýšení úhlu otočení
    úhel -= 1
    print(úhel)

    # Ovládání frekvence snímků
    pygame.time.Clock().tick(60)
