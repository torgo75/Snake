#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

#*********************************************************************
#* Program: Snake - Marc's Version
#* Author: Marc Becker
#* Date: 02.09.2017
#* Description: Copy of the fames Snake Game with the goal to integrate:
#* - Random generator for the Fruits to eat with some gadgets like
#* -- Snake add two items
#* -- Snake moves faster
#* -- Snake can exit at one wall enter on the other side
#**********************************************************************

# Class Snake
# List contain Snake elements, two dimensions for position of each elements
# Add Snake Items, remove Snake Item, Speed, wall jump

#*******************
#Import Bereich, pygame für GUI
#*******************

import pygame, sys, random
#from random import *
from pygame.locals import *

#Globale Variables -- gooing in to Main
WWITH = 800  #Size of the Window (with)
WHIGH = 600 #Size of the Window (high)
BOX = 20    #Size of one Fruit,Snakeitem etc.
FPS = 10    #30 Frames per Second
pygame.init()
DISPLAY=pygame.display.set_mode((WWITH, WHIGH))

#COLOR's       R       G      B
BLACK       =(0      ,0      ,0)
WHITE       =(255    ,255    ,255)
YELLOW      =(1      ,125    ,125)
RED         =(255    ,0      ,0)
LIGHTGREEN  =(0      ,128    ,0)
GREEN       =(0      ,255    ,0)
BLUE        =(0      ,0      ,255)



class window(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("SNAKE - MAB\'s Version")


class snake(object):
    #Variables


    def __init__(self,SCREEN):
        self.speed = 2  # Speed of the Snake
        self.walljump = False  #True = Walljump possible, false = Game end with wall contact
        self.snake = []
        self.snake.append([random.randint(0,WWITH),random.randint(0,WHIGH)])
        self.SNAKERECT = pygame.Rect(self.snake[0][0],self.snake[0][1],BOX,BOX)
        pygame.draw.rect(SCREEN,LIGHTGREEN,self.SNAKERECT)

    #def add(self):
        #adding an Item at the end of the list

    def snakemove(self,SCREEN,direction=(K_RIGHT)):

        snakepaint(BLACK,self.snake[len(self.snake)][0],self.snake[len(self.snake)][1])
        if direction in (K_RIGHT, K_d):
            self.snake[0][0] = self.snake[0][0] + BOX
        elif direction in (K_LEFT, K_a):
            self.snake[0][0] = self.snake[0][0] - BOX
        elif direction in (K_UP, K_w):
            self.snake[0][1] = self.snake[0][1] - BOX
        elif direction in (K_DOWN, K_s):
            self.snake[0][1] = self.snake[0][1] + BOX

        self.snakepaint(LIGHTGREEN,self.snake[0][0],self.snake[0][1])

    def snakepaint (self,color,itemx,itemy):
        self.SNAKERECT=pygame.Rect(itemx,itemy,BOX,BOX)
        pygame.draw.rect(SCREEN,color,self.SNAKERECT)


#class containing the field

class feld(object):
    feld = []

    def __init__(self):
        feld.append([])
        feld.append([])
        feld[0].append(100)
        feld[0].append(100)

class fruit(object):
    #Fruits for the snake, apple = faster, cherry = longer, lucky = faster,walljump or longer

    def __init__(self,DISPLAY):
        fruittypes=["apple", "cherry", "beam", "lucky"]
        fruitx = random.randint(0,WHIGH-BOX)
        fruity = random.randint(0,WHIGH-BOX)
        FRUITRECT = pygame.Rect(fruitx,fruity,BOX,BOX)
        option=fruittypes[random.randint(0,len(fruittypes)-1)]

        if option in "apple":
            pygame.draw.rect(DISPLAY,GREEN,FRUITRECT)
        if option in "cherry":
            pygame.draw.rect(DISPLAY,RED,FRUITRECT)
        if option in "beam":
            pygame.draw.rect(DISPLAY,BLUE,FRUITRECT)
        if option in "lucky":
            pygame.draw.rect(DISPLAY,YELLOW,FRUITRECT)

def main():
    fpsClock = pygame.time.Clock()
    frucht = []
    direction = K_RIGHT
    for i in range(6):
        frucht.append(fruit(DISPLAY))
    schlange = snake(DISPLAY)
    while True:
        print(direction)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                direction=event.key

        schlange.snakemove(DISPLAY,direction)
        pygame.display.update()
        pygame.event.clear()
        fpsClock.tick(FPS)


if __name__ == "__main__":
    main()
