import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Načti obrázek
image = pygame.image.load('stíhačka_do_hry_kanon.png').convert_alpha()
image_rect = image.get_rect()

# Nastav bod pivotu (pravý horní roh na obrazovce)
pivot_pos = (400, 300)  # Můžeš změnit na požadované souřadnice

angle = 0  # Počáteční úhel rotace

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    angle += 1  # Můžeš upravit rychlost rotace

    # Vypočítej ofset od středu obrázku k pravému hornímu rohu
    image_center = pygame.math.Vector2(image_rect.center)
    pivot = pygame.math.Vector2(image_rect.topright)
    offset = pivot - image_center

    # Otoč ofset
    rotated_offset = offset.rotate(-angle)

    # Otoč obrázek
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect()

    # Nastav novou pozici obrázku
    new_center = pygame.math.Vector2(pivot_pos) - rotated_offset
    rotated_rect.center = new_center

    # Vykresli vše
    screen.fill((30, 30, 30))
    screen.blit(rotated_image, rotated_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
