import pygame

class Bullet:
    def __init__(self, x, y, xVel, yVel):
        self.x = x
        self.y = y
        self.xVel = xVel
        self.yVel = yVel

    def move(self):
        self.x -= self.xVel*10
        self.y += self.yVel*10

    def draw(self, screen):
        pygame.draw.circle(screen, (255,0,0), (self.x, self.y), 3)