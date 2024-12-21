# Pygame шаблон - скелет для нового проекта Pygame
import pygame

WIDTH = 1900
HEIGHT = 1000
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

running = True
pygame.draw.circle(screen, RED, (100, 100),10)
pygame.draw.line(screen, BLUE, [10, 30], [290, 15], 3)



f1 = pygame.font.Font(None, 36)
text1 = f1.render('Привет Мир!', True,
                  GREEN)
screen.blit(text1, (200, 100))

pygame.display.update()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()