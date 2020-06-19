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

dist=170
car_w=92
car_h=46
car_vel=5

y_row1=80
y_row2=130
y_row3=270
y_row4=370
y_row5=470

row1=[Car(0,y_row1,car_w,car_h,car_vel,width),
      Car(-dist-car_w,y_row1,car_w,car_h,car_vel,width),
      Car((-dist-car_w)*2,y_row1,car_w,car_h,car_vel,width),
      Car((-dist-car_w)*3,y_row1,car_w,car_h,car_vel,width)]

row2=[Car(width,y_row2,car_w,car_h,car_vel,width),
      Car(width+dist+car_w,y_row2,car_w,car_h,car_vel,width),
      Car((width+(dist+car_w)*2),y_row2,car_w,car_h,car_vel,width),
      Car((width+(dist+car_w)*3),y_row2,car_w,car_h,car_vel,width)]

row3=[Car(width,y_row3,car_w,car_h,car_vel,width),
      Car(width+dist+car_w,y_row3,car_w,car_h,car_vel,width),
      Car((width+(dist+car_w)*2),y_row3,car_w,car_h,car_vel,width),
      Car((width+(dist+car_w)*3),y_row3,car_w,car_h,car_vel,width)]

row4=[Car(0,y_row4,car_w,car_h,car_vel,width),
      Car(-dist-car_w,y_row4,car_w,car_h,car_vel,width),
      Car((-dist-car_w)*2,y_row4,car_w,car_h,car_vel,width),
      Car((-dist-car_w)*3,y_row4,car_w,car_h,car_vel,width)]

row5=[Car(width,y_row5,car_w,car_h,car_vel,width),
      Car(width+dist+car_w,y_row5,car_w,car_h,car_vel,width),
      Car((width+(dist+car_w)*2),y_row5,car_w,car_h,car_vel,width),
      Car((width+(dist+car_w)*3),y_row5,car_w,car_h,car_vel,width)]

cars=[row1,
      row2,
      row3,
      row4,
      row5]

clock=pygame.time.Clock()
pig=Player( 380,
            530,
            64,70,
            7,
            pig_animation,
            width,
            heigth
            )

run=True
while run:
    clock.tick(120)
    pig.move()
    pig.show(screen)

    for car in row1:
        car.move("right",dist)
        car.show(screen,"right")
        if pygame.Rect.colliderect(car.hitbox,pig.hitbox):
            run=False
            for q in range(0,100):
                print("YOU HAVE BEEN INVESTED!!! TRY AGAIN ")

    
    for car in row2:
        car.move("left",dist)
        car.show(screen,"left")
        if pygame.Rect.colliderect(car.hitbox,pig.hitbox):
            run=False
            for q in range(0,100):
                print("YOU HAVE BEEN INVESTED!!! TRY AGAIN ")
    
    for car in row3:
        car.move("left",dist)
        car.show(screen,"left")
        if pygame.Rect.colliderect(car.hitbox,pig.hitbox):
            run=False
            for q in range(0,100):
                print("YOU HAVE BEEN INVESTED!!! TRY AGAIN ")
    
    for car in row4:
        car.move("right",dist)
        car.show(screen,"right")
        if pygame.Rect.colliderect(car.hitbox,pig.hitbox):
            run=False
            for q in range(0,100):
                print("YOU HAVE BEEN INVESTED!!! TRY AGAIN ")
  
    for car in row5:
        car.move("left",dist)
        car.show(screen,"left")
        if pygame.Rect.colliderect(car.hitbox,pig.hitbox):
            run=False
            for q in range(0,100):
                print("YOU HAVE BEEN INVESTED!!! TRY AGAIN ")
 
    if pig.y<=20:
        run=False
        for q in range(0,100):
            print("YOU HAVE CROSSED THE ROAD!!! ")

    pygame.display.update()
    screen.blit(pygame.transform.scale(back,(width,heigth)),(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

pygame.quit()