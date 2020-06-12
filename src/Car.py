import pygame

class Car():

    def __init__(self,x,y,w,h,vel,sprite,s_w):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.vel=vel
        self.sprite=sprite
        self.s_w=s_w

    def move(self,direction):
        if direction=="left":
            if self.x>0-self.w:
                self.x-=self.vel
            else:
                self.x=self.s_w+self.w+100

        

    