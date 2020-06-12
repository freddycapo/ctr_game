import pygame
from pygame import *
import random

from Car import Car
from Player import Player

width=800
heigth=600

screen=pygame.display.set_mode((width,heigth))
pygame.display.set_caption("Cross the road")

run=True
while run:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

pygame.quit()