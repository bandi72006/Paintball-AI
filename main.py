import pygame  
from player import *  

pygame.init()  
screen = pygame.display.set_mode((1280,720))  
pygame.display.set_caption('Paintball')

run = True

player = Player(500,500)

while run:  
    screen.fill((0,150,0))
    player.move()
    player.draw(screen)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run  = False

    pygame.display.flip()  