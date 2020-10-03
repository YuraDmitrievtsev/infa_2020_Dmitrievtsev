import pygame
import numpy as np

pygame.init()

FPS = 30
#Размер окна
sc = pygame.display.set_mode((1750//2, 1000//2))

#Задаем цвета
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

#Белый фон
sc.fill(WHITE)

#Функция рисующая мужика
def DRAW_PUNK(x, hair_color, shirt_color, eye_color):
    #Руки
    pygame.draw.line(sc, YELLOW, [300//2+x//2, 800//2], [100//2+x//2, 100//2], 30//2)
    pygame.draw.line(sc, YELLOW, [700//2+x//2, 800//2], [900//2+x//2, 100//2], 30//2)
    #Майка
    pygame.draw.circle(sc, shirt_color, (500//2+x//2, 1000//2), 350//2)
    #Голова
    pygame.draw.circle(sc, YELLOW, (500//2+x//2, 500//2), 200//2)
    #Ладошки
    pygame.draw.circle(sc, YELLOW, (100//2+x//2, 100//2), 50//2)
    pygame.draw.circle(sc, YELLOW, (900//2+x//2, 100//2), 50//2)
    #Табличка
    pygame.draw.polygon(sc, GREEN, [[30//2+x//2, 100//2], [30//2+x//2, 0//2], [970//2+x//2, 0//2], [970//2+x//2, 100//2]])
    #1 Рукав майки
    x0=280//2+x//2 #задаем центр и радиус описанной окружности правильного пятигольника
    y0=730//2
    r=90//2
    a=2*np.pi/5 #пятая часть 360 градусов для смещения
    POL=[]
    for i in range(5):
        POL.append([x0+r*np.cos(a*i),y0+r*np.sin(a*i)])
    pygame.draw.polygon(sc, shirt_color, POL)
    #2 Рукав майка
    x0=720//2+x//2 #Аналогично для второго
    y0=730//2
    r=90//2
    a=2*np.pi/5
    POL=[]
    for i in range(5):
        POL.append([x0-r*np.cos(a*i),y0-r*np.sin(a*i)])
    pygame.draw.polygon(sc, shirt_color, POL)
    #Рот
    pygame.draw.polygon(sc, RED, [[500//2+x//2,650//2],[400//2+x//2,600//2],[600//2+x//2,600//2]])
    #Глаза
    pygame.draw.circle(sc, eye_color, (425//2+x//2, 450//2), 50//2)
    pygame.draw.circle(sc, eye_color, (575//2+x//2, 450//2), 50//2)
    pygame.draw.circle(sc, BLACK, (425//2+x//2, 450//2), 20//2)#черные зрачки
    pygame.draw.circle(sc, BLACK, (575//2+x//2, 450//2), 20//2)
    #Нос
    pygame.draw.polygon(sc, BROWN, [[500//2+x//2,550//2],[480//2+x//2,500//2],[520//2+x//2,500//2]])
    #Рисование волос
    alpha=np.pi/5 #угол между направлением вправо и направлением на первый волосок
    n=10 #количество волосков -1
    dalpha=(np.pi-2*alpha)/n #угол между соседними волосками
    r=50//2 #радиус описанного треугольного волоса
    a=2*np.pi/3 #треть полного угла для смещения внутри волоса
    for i in range(n+1):
        POL=[]
        x0 = 500//2+(200 +20) * np.cos(alpha)//2 #Координаты центра треугольного волоса
        y0 = 500//2-(200 +20) * np.sin(alpha)//2
        for j in range(3):
            POL.append([x0 + r * np.cos(a * j+alpha)+x//2,y0 - r * np.sin(a * j+alpha)])
        pygame.draw.polygon(sc, hair_color, POL)
        alpha+=dalpha


DRAW_PUNK(0, PINK, ORANGE, BLUE) #Рисование людей
DRAW_PUNK(800, BLUE, RED, GREEN)

#Рисование надписи
font = pygame.font.Font(None, 100//2)
text = font.render("Python is REALLY SUPER DUPER AMAZING!!!", True, BLACK)
textpos = (150//2, 25//2)
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