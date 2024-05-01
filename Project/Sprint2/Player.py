import pygame

class Player:
    def __init__(self, color, radius):

        self.color = color
        self.radius = radius

    def draw(self, screen,x,y):
        pygame.draw.circle(screen, self.color, (x, y), self.radius)
