import pygame
from Character import CharacterImage


class Cave:
    def __init__(self):
        self.image = pygame.image.load(CharacterImage.PIRATE.value)


