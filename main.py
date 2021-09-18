import pygame
from pygame.constants import K_SPACE  
import random

from player import *
from bullet import *  
from target import *


pygame.init()  
screen = pygame.display.set_mode((1280,720))  
pygame.display.set_caption('Paintball')

#Sets up FPS manager to keep it at 60 always
fpsClock = pygame.time.Clock()
FPS = 60

run = True

player = Player(640, 360)

bullets = []
bulletClock = 0

target = Target(random.randint(0,1280), random.randint(0,720))

while run:  
    keys = pygame.key.get_pressed()
    if keys[K_SPACE]:
        if len(bullets) <=  10:
            if bulletClock > 15:
                bullets.append(Bullet(player.x, player.y, player.xVel, player.yVel))
                bulletClock = 0


    player.move()

    for bullet in bullets:
        bullet.move()

        if target.hit(bullet):
            bullets.remove(bullet)

        if bullet.x >= 1280:
            bullets.remove(bullet)
        elif bullet.x <= 0:
            bullets.remove(bullet)

        elif bullet.y >= 720:
            bullets.remove(bullet)
        elif bullet.y <= 0:
            bullets.remove(bullet)

    bulletClock += 1

    #Animation code

    screen.fill((0,150,0))

    target.draw(screen)
    player.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run  = False

    fpsClock.tick(FPS)

    pygame.display.flip()  