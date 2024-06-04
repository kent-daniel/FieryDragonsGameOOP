from typing import Tuple

import pygame.sprite
from Player import Player
from GameConstants import GameImage, GameElementStyles, CharacterImage
from Tile import Tile


class Cave(Tile):
    def __init__(self,
                 id: int,
                 cave_owner: Player,
                 character: CharacterImage,
                 image: str = GameImage.CAVE.value,
                 height: int = GameElementStyles.CAVE_SIZE.value, width: int = GameElementStyles.CAVE_SIZE.value):
        super().__init__(id, character, width, height)

        self._cave_owner = cave_owner
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

    def get_owner(self):
        return self._cave_owner

    def get_surface(self) -> pygame.Surface:
        return self._surface

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self._rect.center = location
        destination_surface.blit(self._surface, self._rect.topleft)

    def redraw_view(self) -> None:
        if self._occupant == self._cave_owner:
            self._draw_player()

    def is_cave(self) -> bool:
        return True


    def _draw_player(self) -> None:
        pass
