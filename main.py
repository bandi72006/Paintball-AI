import pygame
from pygame.constants import K_SPACE  
import random
import os
import neat

from player import *
from bullet import *  
from target import *


pygame.init()  
screen = pygame.display.set_mode((1280,720))  
pygame.display.set_caption('Paintball')

#Sets up FPS manager to keep it at 60 always
fpsClock = pygame.time.Clock()
FPS = 60


def main(genomes, config):
    run = True
    frames = 0

    nets = []
    ge = []
    players = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        players.append(Player(640,360))
        g.fitness = 0
        ge.append(g)

    bullets = []
    bulletClock = 0

    target = Target(random.randint(0,1280), random.randint(0,720))

    while run:  

        frames += 1

        keys = pygame.key.get_pressed()
        for player in players:
            #if keys[K_SPACE]:
            if player.shot == True:
                if len(bullets) <=  10:
                    if bulletClock > 15:
                        bullets.append(Bullet(player.x, player.y, player.xVel, player.yVel))
                        bulletClock = 0
                        player.shot = False


            player.move()
            output = nets[players.index(player)].activate((player.x, player.y, target.x, target.y))

            if output[0] > 0.5: #tanh =-> [-1, 1] so 0.5 = 75%
                player.right()        
            if output[1] > 0.5: #tanh =-> [-1, 1] so 0.5 = 75%
                player.left()
            if output[2] > 0.5: #tanh =-> [-1, 1] so 0.5 = 75%
                player.straight()        
            if output[3] > 0.5: #tanh =-> [-1, 1] so 0.5 = 75%
                player.shoot()

        for bullet in bullets:
            bullet.move()

            for g in ge:
                if target.hit(bullet):
                    bullets.remove(bullet)
                    g.fitness += 10

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
        for player in players:
            player.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                run  = False
                pygame.quit()
                quit()

        fpsClock.tick(FPS)

        pygame.display.flip()

        if frames >= 600:
            players = []
            nets = []
            ge = []
            run = False
            break

def run(configFile):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                    neat.DefaultSpeciesSet, neat.DefaultStagnation,
                    configFile)

    population = neat.Population(config)

    #Output to console
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    winner = population.run(main, 50)

if __name__ == "__main__":
    localDir = os.path.dirname(__file__) #Give us path to current directory
    configPath = os.path.join(localDir, "config-feedforward.txt")
    run(configPath)