import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

image = pygame.Surface((100, 50), pygame.SRCALPHA)  # Vytvoříme jednoduchý obdélník
image.fill((255, 0, 0))
original_rect = image.get_rect()

pivot_pos = (400, 300)  # Umístíme pravý horní roh do středu obrazovky
angle = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    angle += 1  # Nebo použij vstup z klávesnice pro úpravu úhlu

    # Výpočet ofsetu
    image_center = pygame.math.Vector2(original_rect.center)
    pivot = pygame.math.Vector2(original_rect.topright)
    offset = pivot - image_center

    rotated_offset = offset.rotate(-angle)

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect()

    new_center = pygame.math.Vector2(pivot_pos) - rotated_offset
    rotated_rect.center = new_center

    screen.fill((30, 30, 30))
    screen.blit(rotated_image, rotated_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
