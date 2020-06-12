import pygame
from pygame import *

class Player():

    def __init__(self,x,y,w,h,vel,sprite,s_w,s_h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.vel=vel
        self.sprite=sprite
        self.s_w=s_w
        self.s_h=s_h

        self.walkcount=0

    def move(self):
        keys=pygame.key.get_pressed()
        
        if keys[K_UP] or keys[K_w]:
            if self.y>0:
                self.y-=self.vel
        elif keys[K_DOWN] or keys[K_s]:
            if self.y<self.s_h-self.h:
                self.y+=self.vel
        elif keys[K_RIGHT] or keys[K_d]:
            if self.x<self.s_w:
                self.x+=self.vel
        elif keys[K_LEFT] or keys[K_a]:
            if self.x>0:
                self.x-=self.vel
        self.walkcount+=1

    def show(self,screen):
        if self.walkcount +1 >= 6:
            self.walkcount=0
        
        cur_frame=self.sprite[self.walkcount//3]
        screen.blit(pygame.transform.scale(cur_frame,(self.w,self.h)),(self.x,self.y))
        pygame.display.update()
