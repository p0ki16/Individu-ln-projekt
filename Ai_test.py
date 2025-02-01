import pygame
import random
import math

class Square:
    def __init__(self, x, y, image_path, speed, angle):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = speed
        self.angle = angle

    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface,image):
        surface.blit(image, self.rect)

# Inicializace Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Samostatně se pohybující obrázky")
clock = pygame.time.Clock()

# Vytvoření čtverců s obrázky
squares = []
image_paths = ['kanon_stíhačka.png', 'strela.png', 'kanon_2l3.png']  # Nahraď vlastními cestami k obrázkům
kanon43 = pygame.image.load("kanon_4l3.png")
for _ in range(10):  # Počet obrázků
    x = random.randint(0, 750)
    y = random.randint(0, 550)
    image_path = random.choice(image_paths)
    speed = random.uniform(1, 5)
    angle = random.uniform(0, 360)
    square = Square(x, y, image_path, speed, angle)
    squares.append(square)

# Hlavní smyčka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for square in squares:
        square.move()
        square.draw(screen,kanon43)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
