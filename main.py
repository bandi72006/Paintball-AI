import pygame  
from player import *  

pygame.init()  
screen = pygame.display.set_mode((1280,720))  
pygame.display.set_caption('Paintball')

#Sets up FPS manager to keep it at 30 always
#fpsClock = pygame.time.Clock()
#FPS = 30

run = True

player = Player(500,500)

while run:  
    screen.fill((0,150,0))
    player.move()
    player.draw(screen)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run  = False

    #fpsClock.tick(FPS)

    pygame.display.flip()  