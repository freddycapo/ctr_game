import pygame

class Car():

    def __init__(self,x,y,w,h,vel,s_w):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.vel=vel
        self.s_w=s_w

        self.hitbox=pygame.Rect(self.x+30,self.y+30,self.w-30,self.h-30)

    def move(self,direction,dist):
        if direction=="right":
            if self.x<self.s_w:
                self.x+=self.vel
            else:
                self.x=0-dist-self.w
        elif direction=="left":
            if self.x>0-self.w:
                self.x-=self.vel
            else:
                self.x=self.s_w+dist+self.w

    def show(self,screen,direction):
        if direction=="left":
            image=pygame.image.load("src\images\car.png")
        elif direction=="right":
            image=pygame.image.load("src\images\car_right.png")

        screen.blit(pygame.transform.scale(image,(self.w,self.h)),(self.x,self.y))
        self.hitbox=pygame.Rect(self.x+5,self.y+5,self.w-5,self.h-5)
        pygame.draw.rect(screen,(0,0,255),self.hitbox,1)
        