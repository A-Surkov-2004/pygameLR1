# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

# importing the module
import numpy as np

# creating two matrices
print('Введите 2 числа через пробел (не меньше 15)')
x,y = map(int, input().split())


p = [[x],[y]]
q = [[1, 3], [4, 1]]
result = np.dot(q, p)


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
pygame.draw.circle(screen, RED, (p[0][0], p[1][0]),10)
pygame.draw.circle(screen, BLUE, (result[0][0], result[1][0]),10)
pygame.display.update()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()