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


p = [[2,-2],[-2,-2],[-2,2],[2,2]]
q = [[0.9, 0], [0, 0.9]]
q2 = [[math.cos(math.pi/32), -math.sin(math.pi/32)], [math.sin(math.pi/32), math.cos(math.pi/32)]]

for i in p:
    i[0] = i[0]*100
    i[1] = i[1]*100

result = p

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

def move2center(v):
    for i in v:
        i[0] += WIDTH/2
        i[1] += HEIGHT/2



move2screen(p)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

running = True

pygame.draw.polygon(screen, RED, ((p[0][0], p[0][1]),(p[1][0], p[1][1]), (p[2][0], p[2][1]), (p[3][0], p[3][1])),10)

cx = (p[0][0]-p[1][0])/2

cy = (p[3][1]-p[0][1])/2

for i in p:
    print(i)

print(f'cx = {cx}')
print(f'cy = {cy}')

for i in range(20):
    p = result
    for i in p:
        i[0]-= cx
        i[1] -= cy
    result = np.dot(p, q)
    result = np.dot(result, q2)
    for i in result:
        i[0] += cx
        i[1] += cy
    #move2screen(result)
        #i[1]+= 0.1*i[1]

    pygame.draw.polygon(screen, BLUE, ((result[0][0], result[0][1]),(result[1][0], result[1][1]), (result[2][0], result[2][1]),(result[3][0], result[3][1])),10)
    #input()
    pygame.display.update()




pygame.display.update()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()