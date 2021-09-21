#Bandar Al Aish

import pygame
import math
import random

from bullet import *
from target import *

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xVel = 0
        self.yVel = 0
        self.speed = 0
        self.rotation = 0
        self.rotationSpeed = 5
        self.bullets = []
        self.bulletClock = 0
        self.target = Target(random.randint(0,1280), random.randint(0,720))

    def move(self, g):
        self.bulletClock += 1
        keys = pygame.key.get_pressed()
        
        #if keys[pygame.K_UP] or keys[pygame.K_w]:
        #    if self.speed <= 7:
        #        self.speed += 0.4
        if self.speed > 0:
            self.speed -= 0.5
        else: 
            self.speed = 0

        #if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        #    self.rotation -= self.rotationSpeed

        
        #if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        #    self.rotation += self.rotationSpeed

        self.xVel = math.cos(math.radians(self.rotation)) #have to convert degrees to radians
        self.yVel = math.sin(math.radians(self.rotation))

        self.x -= self.xVel*self.speed
        self.y += self.yVel*self.speed

        if self.x >= 1280:
            self.x = 1
        if self.x <= 0:
            self.x = 1279

        if self.y >= 720:
            self.y = 1
        if self.y <= 0:
            self.y = 719

        for bullet in self.bullets:
            bullet.move()
            
            if bullet.x >= 1280:
                self.bullets.remove(bullet)
            elif bullet.x <= 0:
                self.bullets.remove(bullet)

            elif bullet.y >= 720:
                self.bullets.remove(bullet)
            elif bullet.y <= 0:
                self.bullets.remove(bullet)

            elif self.target.hit(bullet):
                    self.bullets.remove(bullet)
                    g.fitness += 10

    def right(self):
        self.rotation -= self.rotationSpeed

    def left(self):
        self.rotation += self.rotationSpeed

    def straight(self):
        if self.speed <= 7:
            self.speed += 0.4

    def shoot(self):
        if len(self.bullets) <=  10:
            if self.bulletClock > 15:
                self.bullets.append(Bullet(self.x, self.y, self.xVel, self.yVel))
                self.bulletClock = 0


    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y), 20)
        pygame.draw.circle(screen, (0,0,0), (self.x - math.cos(math.radians(self.rotation))*17, self.y + math.sin(math.radians(self.rotation))*17),2)
        for bullet in self.bullets:
            bullet.draw(screen)
        self.target.draw(screen)