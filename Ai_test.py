import pygame
import sys
import math
test = 10000
# Inicializace Pygame
pygame.init()

# Nastavení rozměrů okna
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kulička následující kurzor")

# Barvy
background_color = (255, 255, 255)  # Bílá
ball_color = (0, 0, 255)  # Modrá

# Parametry kuličky
ball_radius = 15
ball_pos = [400, 300]  # Počáteční pozice kuličky

# Rychlost kuličky
ball_speed = 0.05

# Hlavní smyčka hry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Získání pozice kurzoru myši
    if test>0:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        test-=1
    else:
        mouse_y=650
        
    
    # Výpočet rozdílu v pozicích
    dx = mouse_x - ball_pos[0]
    dy = mouse_y - ball_pos[1]
    
    # Výpočet vzdálenosti mezi kuličkou a kurzorem
    distance = math.sqrt(dx**2 + dy**2)
    
    # Normování směrového vektoru
    if distance != 0:
        dx /= distance
        dy /= distance
    
    # Aktualizace pozice kuličky
    ball_pos[0] += dx * ball_speed
    ball_pos[1] += dy * ball_speed
    
    # Vyplnění pozadí
    screen.fill(background_color)
    
    # Kreslení kuličky na aktuální pozici
    pygame.draw.circle(screen, ball_color, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
    
    # Aktualizace okna
    pygame.display.flip()


