import pygame


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

sc.fill(WHITE)
pygame.draw.circle(sc, YELLOW, (500, 500), 200)
pygame.draw.line(sc, BLACK, [400, 600], [600, 600], 30)
pygame.draw.circle(sc, RED, (450, 450), 75)
pygame.draw.circle(sc, RED, (575, 450), 50)
pygame.draw.circle(sc, BLACK, (450, 450), 50)
pygame.draw.circle(sc, BLACK, (575, 450), 25)
pygame.draw.line(sc, BLACK, [300, 300], [520, 410], 20)
pygame.draw.line(sc, BLACK, [700, 350], [520, 410], 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()