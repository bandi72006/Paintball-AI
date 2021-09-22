import pygame

class Bullet:
    def __init__(self, x, y, xVel, yVel, colour):
        self.x = x
        self.y = y
        self.xVel = xVel
        self.yVel = yVel
        self.colour = colour
        self.radius = 3

    def move(self):
        self.x -= self.xVel*10
        self.y += self.yVel*10

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)