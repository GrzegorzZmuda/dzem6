import numpy as np
import pygame, pygame.rect
import random
import time
import math

class box:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.srf = pygame.image.load("5.bmp")
        self.rect = self.srf.get_rect(topleft=(self.x,self.y))


    def disp(self):
        screen.blit(self.srf, (self.x, self.y))

class ball:
    def __init__(self):
        self.x=395
        self.y=400
        self.dir=270
        self.spd=3
        self.srf=pygame.image.load("2.bmp")
        self.rect = self.srf.get_rect()

    def mov(self):
        self.rect_update()
        if self.dir>360:
            self.dir-=360
        if self.dir < 0:
            self.dir += 360
        if  self.y<0:
            self.dirchange()
        if self.x < 0 or self.x > 800:
            self.dirchange2()
        self.x+=math.sin(math.radians(self.dir+270))
        self.y+=math.sin(math.radians(self.dir+180))
        if self.y>760:
            pygame.quit()
            exit()

    def disp(self):
        screen.blit(self.srf, (self.x, self.y))

    def coltest(self, sprite):
        return self.rect.colliderect(sprite)
    def dirchange(self):
        self.dir+=180+random.randrange(-20,20)

    def dirchange2(self):
        self.dir += 90 + random.randrange(-10, 10)
    def rect_update(self):
        self.rect = self.srf.get_rect(topleft=(self.x,self.y))


class board:
    def __init__(self):
        self.x=375
        self.y=750
        self.srf=pygame.image.load("7.bmp")
        self.rect = self.srf.get_rect()

    def rect_update(self):
        self.rect = self.srf.get_rect(topleft=(self.x,self.y))


    def mov(self, dir):
        self.rect_update()
        if dir==True and self.x<700:
            self.x+=2
        if dir==False and self.x>0:
            self.x-=2

    def disp(self):
        screen.blit(self.srf, (self.x, self.y))
map=[]
for i in range(10):

    for j in range(20):
        if 1==random.randrange(0,5):
            map.append(box(j*40,i*20))

pygame.init()
surf1=np.full((800,800,3),(230,239,230))
surf2 = pygame.surfarray.make_surface(surf1)

screen = pygame.display.set_mode((800,800))
font = pygame.font.Font('freesansbold.ttf', 20)
Running=True
screen.blit(surf2, (0, 0))
flag=False
b=board()
bl=ball()
points=0
mul=1

while Running:

    #  start
    while flag==False:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q] and keys[pygame.K_w] and keys[pygame.K_e] and keys[pygame.K_r] and keys[pygame.K_t]:
                flag=True
    c=time.time()

    screen.blit(surf2, (0, 0))
    temp=0
    for boxes in map:
        temp=temp+1
        boxes.disp()

        if bl.coltest(boxes.rect):
            bl.dirchange()
            map=map[0:temp-1]+map[temp:len(map)]

            points=points+mul
            mul = mul + 1
            break



    if bl.coltest(b):
        bl.dirchange()
        mul=1
        bl.mov()
        bl.mov()
        bl.mov()
        bl.mov()
    font1 = pygame.font.Font('freesansbold.ttf', 50)
    text1 = font1.render("TETRIS", True, (200, 200, 200), (230,239,230))
    screen.blit(text1, (300, 400))
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(str(points), True, (20, 20, 20), (230,239,230))
    screen.blit(text, (0, 770))
    bl.mov()
    bl.disp()
    b.disp()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        b.mov(False)

    if keys[pygame.K_d]:
        b.mov(True)

    while time.time()-c<0.003:
        a=1



