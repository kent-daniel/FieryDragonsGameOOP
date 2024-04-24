from typing import Tuple

import pygame.sprite
from Player import Player
import GameConstants
from Drawable import Drawable

class Cave(Drawable):
    def __init__(self, cave_owner: Player, image: str, height: int , width: int, colour: pygame.Color):
        self._caveOwner = cave_owner
        self._surface: pygame.Surface = pygame.Surface((height, width), pygame.SRCALPHA)
        self._image: pygame.Surface = pygame.image.load(image).convert_alpha()

        pygame.draw.rect(self._surface,
                         self._caveOwner.colour,
                         self._surface.get_rect(),
                         )
        self._surface.blit(self._image, self._image.get_rect(center=(height // 2, width // 2)))
        self._rect: pygame.Rect = self._surface.get_rect()


    def get_surface(self) -> pygame.Surface:
        pass

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        pass