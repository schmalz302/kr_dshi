import pygame
import os
from random import choice

a = {}
b = []
cc = 0
for i in os.listdir('художники'):
    a[i] = []
    b.append(i)
    for j in os.listdir(f'художники/{i}'):
        a[i].append(j)
    cc += len(a[i])
c = []
pygame.init()
screen = pygame.display.set_mode((700, 1000))
screen.fill((255, 255, 255))
FPS = 50
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x = choice(b)
                y = choice(a[x])
                while f'{x}/{y}' in c:
                    x = choice(b)
                    y = choice(a[x])
                c.append(f'{x}/{y}')
                print(f'{x}/{y}')
                aa = pygame.image.load(
                    f'художники/{x}/{y}')
                bb = aa.get_rect()
                screen.fill((255, 255, 255))
                if bb[2] > 700:
                    bb2 = int(bb[3] / (bb[2] / 700))
                    screen.blit(pygame.transform.scale(aa, (700, bb2)), (0, 0))
                else:
                    screen.blit(aa, (0, 0))
    pygame.display.flip()
pygame.quit()
