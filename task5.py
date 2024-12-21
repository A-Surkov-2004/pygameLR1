# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import math

# importing the module
import numpy as np

# creating two matrices
print('Введите 2 числа через пробел (не меньше 15)')


p = [[50,100],[250,200],[50,200],[250,300]]
q = [[1, 2], [3, 1]]
result = np.dot(p, q)


WIDTH = 1900
HEIGHT = 1000
FPS = 30
# Задаем цвета
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
pygame.draw.line(screen, RED, (p[0][0], p[0][1]), (p[1][0], p[1][1]),10)
pygame.draw.line(screen, RED, (p[2][0], p[2][1]), (p[3][0], p[3][1]),10)
dx = abs(p[0][0]-p[1][0])
dy = abs(p[0][1]-p[1][1])
deg = (math.atan(dy/dx) * 57.3)%360

f1 = pygame.font.Font(None, 36)
text1 = f1.render(f'{deg}°', True,
                  GREEN)
screen.blit(text1, (200, 100))



pygame.draw.line(screen, BLUE, (result[0][0], result[0][1]), (result[1][0], result[1][1]),10)
pygame.draw.line(screen, BLUE, (result[2][0], result[2][1]), (result[3][0], result[3][1]),10)

dx = abs(result[0][0]-result[1][0])
dy = abs(result[0][1]-result[1][1])
deg = (math.atan(dy/dx) * 57.3)%360

f1 = pygame.font.Font(None, 36)
text1 = f1.render(f'{deg}°', True,
                  GREEN)
screen.blit(text1, (700, 300))




pygame.display.update()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()