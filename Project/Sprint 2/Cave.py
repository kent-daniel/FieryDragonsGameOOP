from typing import Tuple

import pygame.sprite
from Player import Player
from GameConstants import GameImage , GameStyles , GameElementStyles
from Drawable import Drawable

class Cave(Drawable):
    def __init__(self, cave_owner: Player, image: str = GameImage.CAVE.value, height: int = GameElementStyles.CAVE_SIZE.value, width: int = GameElementStyles.CAVE_SIZE.value):
        self._caveOwner = cave_owner
        self._surface: pygame.Surface = pygame.Surface((height, width), pygame.SRCALPHA)
        self._image: pygame.Surface = pygame.image.load(image).convert_alpha()
        self._image = pygame.transform.smoothscale(self._image, (width, height))
        self._surface.blit(self._image, self._image.get_rect(center=(height // 2, width // 2)))
        self._rect: pygame.Rect = self._surface.get_rect()
        pygame.draw.circle(self._surface,
                           cave_owner.colour,
                           self._rect.center,
                           radius=height // 2,  # Radius (slightly larger than the cave)
                           width=5)




    def get_surface(self) -> pygame.Surface:
        return self._surface

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self._rect.center = location
        destination_surface.blit(self._surface, self._rect.topleft)