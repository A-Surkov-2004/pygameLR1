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

p = []

a = 5
b = 3



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

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

running = True
for i in range(1, 1000):
    f = i*1
    r = b + 2 * a * math.cos(f)
    x = r * math.cos(f) * 60 + WIDTH/3
    y = r * math.sin(f) * 60 + HEIGHT/2
    now = [x, y]
    pygame.draw.circle(screen, RED, now, 1)
    p.append(now)





pygame.display.update()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()