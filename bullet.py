import pygame

class Bullet:
    def __init__(self, x, y, xVel, yVel):
        self.x = x
        self.y = y
        self.xVel = xVel
        self.yVel = yVel

    def move(self):
        self.x -= self.xVel*2
        self.y += self.yVel*2

        if self.x >= 1280:
            self.x = 1
        if self.x <= 0:
            self.x = 1279

        if self.y >= 720:
            self.y = 1
        if self.y <= 0:
            self.y = 719

    def draw(self, screen):
        pygame.draw.circle(screen, (255,0,0), (self.x, self.y), 3)