import pygame
# Nastavení okna
WIDTH, HEIGHT = 800, 600
obrazovka = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Načtení obrázku
atom = pygame.image.load("atom_výbuch.png")
original_width, original_height = atom.get_size()

# Počáteční velikost
obrazek_x = original_width
obrazek_y = 50  # Začíná malý

# Počáteční pozice (zarovnaný dole)
x_pos = 400  # X souřadnice obrázku
y_pos = HEIGHT - obrazek_y  # Y souřadnice obrázku (odspoda)

running = True
while running:
    obrazovka.fill((255, 255, 255))  # Vymazání obrazovky

    # Zvětšování obrázku odspoda
    if obrazek_y < original_height:
        obrazek_y += 5
        y_pos = HEIGHT - obrazek_y  # Posunout horní okraj nahoru

    # Přizpůsobení velikosti obrázku
    resized_atom = pygame.transform.scale(atom, (obrazek_x, obrazek_y))

    # Vykreslení obrázku na nové pozici
    obrazovka.blit(resized_atom, (x_pos, y_pos))

    pygame.display.update()  # Aktualizace obrazovky

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(30)  # Omezí FPS

pygame.quit()