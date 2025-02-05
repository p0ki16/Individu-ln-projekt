import pygame
import sys

# Inicializace Pygame
pygame.init()

# Nastavení rozměrů okna
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Více tlačítek v Pygame")

# Barvy
background_color = (255, 255, 255)  # Bílá
button_color = (0, 0, 255)  # Modrá

class Button:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    
    def draw(self, screen):
        pygame.draw.rect(screen, button_color, self.rect)
    
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# Vytvoření tlačítek
buttons = [
    Button(100, 100, 200, 50),
    Button(100, 200, 200, 50),
    Button(100, 300, 200, 50),
]

# Hlavní smyčka hry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for button in buttons:
            if button.is_clicked(event):
                print(f"Tlačítko {buttons.index(button) + 1} bylo kliknuto")

    # Vyplnění pozadí
    screen.fill(background_color)
    
    # Vykreslení tlačítek
    for button in buttons:
        button.draw(screen)
    
    # Aktualizace okna
    pygame.display.flip()
