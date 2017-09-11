#!/usr/bin/python3

import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800,600))
xpos =800/2-5
ypos = 600/2-5
box = 20
myColor =(230,220,10)
black = (0,0,0)
myRect = pygame.Rect(xpos,ypos,box,box)
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            pygame.display.set_caption('****** Hello Asterisk *******')
            if event.key in (K_RIGHT, K_d):
                pygame.draw.rect(DISPLAYSURF,black,myRect)
                xpos = xpos + 20
                myRect = pygame.Rect(xpos,ypos,box,box)
                pygame.draw.rect(DISPLAYSURF,myColor,myRect)
            elif event.key in(K_LEFT, K_a):
                pygame.draw.rect(DISPLAYSURF,black,myRect)
                xpos = xpos - 20
                myRect = pygame.Rect(xpos,ypos,box,box)
                pygame.draw.rect(DISPLAYSURF,myColor,myRect)
            elif event.key in(K_UP, K_w):
                pygame.draw.rect(DISPLAYSURF,black,myRect)
                ypos = ypos - 20
                myRect = pygame.Rect(xpos,ypos,box,box)
                pygame.draw.rect(DISPLAYSURF,myColor,myRect)
            elif event.key in(K_DOWN, K_s):
                pygame.draw.rect(DISPLAYSURF,black,myRect)
                ypos = ypos + 20
                myRect = pygame.Rect(xpos,ypos,box,box)
                pygame.draw.rect(DISPLAYSURF,myColor,myRect)
        pygame.display.update()
