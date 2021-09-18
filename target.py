import pygame
import random

class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20

    def hit(self, bullet):
        if (bullet.x + bullet.radius > self.x-self.radius) and (bullet.x - bullet.radius < self.x + self.radius):
            if (bullet.y + bullet.radius > self.y-self.radius) and (bullet.y - bullet.radius < self.y + self.radius):
                self.x = random.randint(0,1280)
                self.y = random.randint(0,720)
                return True
            else: 
                return False
        else:
            return False

    def draw(self, screen):
        pygame.draw.circle(screen, (200,100,100), (self.x, self.y), self.radius)