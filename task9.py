# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import math

# importing the module
import numpy as np

WIDTH = 1900
HEIGHT = 1000
FPS = 30
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# creating two matrices
print('Введите 2 числа через пробел (не меньше 15)')


p = [[3,-1],[4,1],[2,1]]
q = [[2, 0], [0, 2]]

for i in p:
    i[0] = i[0]*100
    i[1] = i[1]*100

result = np.dot(p, q)

def move2screen(v):
    mx = WIDTH
    my = HEIGHT
    for i in v:
        mx = min(mx,i[0])
        my = min(my,i[1])
    if mx < 0:
        for i in v:
            i[0] -= mx
    if my < 0:
        for i in v:
            i[1] -= my



move2screen(p)
move2screen(result)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

running = True
pygame.draw.polygon(screen, RED, ((p[0][0], p[0][1]),(p[1][0], p[1][1]), (p[2][0], p[2][1])),10)

pygame.draw.polygon(screen, BLUE, ((result[0][0], result[0][1]),(result[1][0], result[1][1]), (result[2][0], result[2][1])),10)





pygame.display.update()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()