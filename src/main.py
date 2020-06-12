import pygame
from pygame import *
import random

from Car import Car
from Player import Player

width=800
heigth=600

screen=pygame.display.set_mode((width,heigth))
pygame.display.set_caption("Cross the road")
back=pygame.image.load("src/images/background.png")
pig_animation=[pygame.image.load("src/images/sprite_pig0.png"),pygame.image.load("src/images/sprite_pig1.png")]

clock=pygame.time.Clock()
pig=Player( 380,
            530,
            64,70,
            5,
            pig_animation,
            width,
            heigth
            )

cars=[[]]

run=True
while run:
    clock.tick(30)
    pig.move()
    pig.show(screen)

    screen.blit(pygame.transform.scale(back,(width,heigth)),(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

pygame.quit()