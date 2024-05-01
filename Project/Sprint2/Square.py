import random

import pygame

from Project.Sprint2.Cave import Cave
from Project.Sprint2.Character import CharacterImage


class Square:
    def __init__(self, x, y, size):
        self.character = random.choice(list(CharacterImage))
        self.x = x
        self.y = y
        self.size = size
        self.image = self.generate_square()
        self.player_here = False
        self.cave = Cave()


    def generate_square(self):
        return pygame.image.load(self.character.value)

    def draw(self, screen):
        resized_image = pygame.transform.scale(self.image, (self.size, self.size))
        screen.blit(resized_image, (self.x, self.y))

    def set_player_here(self, player_here):
        self.player_here = player_here

    def is_player_here(self):
        return self.player_here

    def add_cave(self, screen, x, y, player_name):
        cave_x = self.x + x
        cave_y = self.y + y
        self.cave.display_cave(screen,cave_x,cave_y,self.size, player_name)
