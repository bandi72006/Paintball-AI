import pygame
import random

class Target:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.radius = 5
        self.colour = colour

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
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)