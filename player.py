#Bandar Al Aish

import pygame
import math



class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xVel = 0
        self.yVel = 0
        self.speed = 0
        self.rotation = 0
        self.rotationSpeed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.speed <= 7:
                self.speed += 0.4
        else:
            if self.speed > 0:
                self.speed -= 0.5
            else: 
                self.speed = 0

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotation -= self.rotationSpeed

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotation += self.rotationSpeed

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

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y), 20)
        pygame.draw.circle(screen, (0,0,0), (self.x - math.cos(math.radians(self.rotation))*17, self.y + math.sin(math.radians(self.rotation))*17),2)
