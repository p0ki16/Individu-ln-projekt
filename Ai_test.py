import pygame

# Inicializácia Pygame
pygame.init()

# Nastavenie okna
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Načítanie obrázka
image = pygame.image.load("bomber12.png")  # Nahraď svojím obrázkom
 # Zmenšenie obrázka

# Počiatočné hodnoty
angle = 0
running = True

while running:
    screen.fill((30, 30, 30))  # Vyplnenie pozadia
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Otočenie obrázka
    rotated_image = pygame.transform.rotate(image, angle)
    
    # Centrovanie otočeného obrázka
    rect = rotated_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    # Vykreslenie
    screen.blit(rotated_image, rect.topleft)

    angle += 1  # Zväčšenie uhla o 1 stupeň na animáciu
    pygame.display.update()
    clock.tick(60)  # Obnovovanie 60 FPS

pygame.quit()
