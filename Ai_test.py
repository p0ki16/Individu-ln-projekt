import pygame
import sys

# Inicializace Pygame
pygame.init()

# Nastavení velikosti okna
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Tlačítko s obrázkem")

# Načtení obrázku tlačítka
button_image = pygame.image.load("button_levels.png")  
button_rect = button_image.get_rect(center=(200, 150))  # Umístění obrázku na střed obrazovky

# Hlavní smyčka
while True:
    screen.fill((255, 255, 255))  # Vyplníme pozadí bílou barvou

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Zjištění, zda bylo tlačítko kliknuto
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):  # Kontrola, zda kliknutí bylo na obrázku tlačítka
                print("Tlačítko bylo kliknuto!")

    # Vykreslení tlačítka jako obrázku
    screen.blit(button_image, button_rect)

    # Aktualizace okna
    pygame.display.flip()
