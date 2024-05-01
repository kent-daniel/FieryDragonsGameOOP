import random

import pygame

class Player:
    def __init__(self, radius):

        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = radius

    def draw(self, screen,x,y):
        pygame.draw.circle(screen, self.color, (x, y), self.radius)
