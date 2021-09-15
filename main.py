import pygame
from pygame.constants import K_SPACE  
from player import *
from bullet import *  

pygame.init()  
screen = pygame.display.set_mode((1280,720))  
pygame.display.set_caption('Paintball')

run = True

player = Player(500,500)
bullets = []

while run:  
    keys = pygame.key.get_pressed()
    if keys[K_SPACE]:
        bullets.append(Bullet(player.x, player.y, player.xVel, player.yVel))

    player.move()
    for bullet in bullets:
        bullet.move()
    
    screen.fill((0,150,0))
    player.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run  = False

    pygame.display.flip()  