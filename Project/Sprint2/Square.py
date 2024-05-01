import random

import pygame

from Project.Sprint2.Cave import Cave
from Project.Sprint2.Character import CharacterImage


class Square:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.image = self.generate_square()
        self.player_here = False
        self.cave = Cave()

    def generate_square(self):
        random_image = random.choice(list(CharacterImage))
        return pygame.image.load(random_image.value)

    def draw(self, screen):
        resized_image = pygame.transform.scale(self.image, (self.size, self.size))
        screen.blit(resized_image, (self.x, self.y))

    def set_player_here(self, player_here):
        self.player_here = player_here

    def is_player_here(self):
        return self.player_here


