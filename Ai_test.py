import pygame

# Inicializace Pygame a nastavení okna
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Text Example")
clock = pygame.time.Clock()

# Inicializace fontu
font = pygame.font.SysFont('Arial', 48)

# Vykreslení textu
text_surface = font.render('Hello, Pygame!', True, (255, 255, 255))  # Bílé písmo
text_rect = text_surface.get_rect(center=(400, 300))  # Umístění textu na střed obrazovky

# Hlavní smyčka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))  # Vymaže obrazovku černou barvou
    screen.blit(text_surface, text_rect)  # Vykreslí text
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
