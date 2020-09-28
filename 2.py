import pygame
import numpy as np

pygame.init()

FPS = 30
sc = pygame.display.set_mode((1000, 1000))

WHITE = (255, 255, 255)
RED=(200, 0, 0)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
ORANGE=(255,165,0)
BLUE=(0,0,255)
BROWN=(165,42,42)

sc.fill(WHITE)
pygame.draw.line(sc, YELLOW, [300, 800], [100, 100], 30)
pygame.draw.line(sc, YELLOW, [700, 800], [900, 100], 30)
pygame.draw.circle(sc, ORANGE, (500, 1000), 350)
pygame.draw.circle(sc, YELLOW, (500, 500), 200)
pygame.draw.circle(sc, YELLOW, (100, 100), 50)
pygame.draw.circle(sc, YELLOW, (900, 100), 50)
pygame.draw.polygon(sc, GREEN, [[30, 100], [30, 0], [970, 0], [970, 100]])
pygame.draw.circle(sc, RED, (280, 730), 50)
x0=280
y0=730
r=90
a=2*np.pi/5
POL=[]
for i in range(5):
    POL.append([x0+r*np.cos(a*i),y0+r*np.sin(a*i)])
pygame.draw.polygon(sc, RED, POL)
x0=720
y0=730
r=90
a=2*np.pi/5
POL=[]
for i in range(5):
    POL.append([x0-r*np.cos(a*i),y0-r*np.sin(a*i)])
pygame.draw.polygon(sc, RED, POL)
pygame.draw.polygon(sc, RED, [[500,650],[400,600],[600,600]])
pygame.draw.circle(sc, BLUE, (425, 450), 50)
pygame.draw.circle(sc, BLUE, (575, 450), 50)
pygame.draw.circle(sc, BLACK, (425, 450), 20)
pygame.draw.circle(sc, BLACK, (575, 450), 20)
pygame.draw.polygon(sc, BROWN, [[500,550],[480,500],[520,500]])
alpha=np.pi/5
n=10
dalpha=(np.pi-2*alpha)/n
r=50
a=2*np.pi/3
for i in range(n+1):
    POL=[]
    x0 = 500+(200 +20) * np.cos(alpha)
    y0 = 500-(200 +20) * np.sin(alpha)
    for j in range(3):
        POL.append([x0 + r * np.cos(a * j+alpha),y0 - r * np.sin(a * j+alpha)])
    pygame.draw.polygon(sc, PINK, POL)
    alpha+=dalpha

font = pygame.font.Font(None, 100)
text = font.render("Python is AMAZING!!!", True, BLACK)
textpos = (150, 25)
sc.blit(text, textpos)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()