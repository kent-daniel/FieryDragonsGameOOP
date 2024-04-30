import math

import pygame

class Volcano:
    def __init__(self, width, height, fps):
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption('Fiery Game')
        self.timer = pygame.time.Clock()
        self.fps = fps
        self.dragon_card = DragonCard()

