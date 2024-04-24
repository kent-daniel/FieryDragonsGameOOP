import logging
from typing import Tuple, Optional
import pygame
from GameConstants import CharacterImage, GameElementStyles, GameStyles
from Drawable import Drawable
from Player import Player
from Cave import Cave


class Square(Drawable):
    def __init__(self, id: int, character: CharacterImage, cave: Optional[Cave] = None, width: int = GameElementStyles.SQUARE_LENGTH.value,
                 height: int = GameElementStyles.SQUARE_LENGTH.value) -> None:
        self._id = id
        self._character: CharacterImage = character
        self._next: Optional[Square] = None
        self._prev: Optional[Square] = None
        self._occupant: Optional[Player] = None
        self._cave: Optional[Cave] = cave
        self._rect = None
        self._width = width
        self._height = height
        self._image: pygame.Surface = pygame.image.load(character.value).convert_alpha()
        self._image = pygame.transform.smoothscale(self._image, (width * 0.8, height * 0.8))

        self._square_surface: pygame.Surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self._combined_surface: pygame.Surface = self._square_surface if cave is None else pygame.Surface(
            (width, height + cave.get_surface().get_rect().height), pygame.SRCALPHA)
        self.update_square_surface()

    def update_square_surface(self) -> None:
        self._rect: pygame.Rect = self._combined_surface.get_rect()
        self._draw_square()
        self._draw_cave()
        self._draw_player()


    def _draw_square(self) -> None:
        pygame.draw.rect(self._square_surface,
                     GameStyles.COLOR_BROWN.value,
                     self._square_surface.get_rect(),
                     border_radius=GameStyles.BORDER_RADIUS_MEDIUM.value
                     )
        self._square_surface.blit(self._image, self._image.get_rect(center=(self._square_surface.get_width() // 2, self._square_surface.get_height() // 2)))
        self._combined_surface.blit(self._square_surface, self._rect.topleft)


    def _draw_cave(self) -> None:
        if self._cave is None: return
        self._cave.draw(self._combined_surface, (self._rect.centerx,self._rect.centery+GameElementStyles.CAVE_OFFSET.value))

    def _draw_player(self) -> None:
        if self._occupant is None: return
        self._occupant.draw(self._combined_surface, self._rect.midtop)

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self._rect.topleft = location
        destination_surface.blit(self._combined_surface, self._rect.topleft)

    def get_surface(self) -> pygame.Surface:
        return self._combined_surface

    def get_occupant(self) -> Player or None:
        return self._occupant

    def accept_player(self, player: Player) -> None:
        self._occupant = player
        self.update_square_surface()
    def remove_player(self) -> None:
        self._occupant = None
        self.update_square_surface()
    @property
    def id(self) -> int:
        return self._id

    @property
    def character(self) -> CharacterImage:
        return self._character

    @property
    def next(self) -> 'Square' or None:
        return self._next

    @next.setter
    def next(self, square: 'Square' or None) -> None:
        self._next = square

    @property
    def prev(self) -> 'Square' or None:
        return self._prev

    @prev.setter
    def prev(self, square: 'Square' or None) -> None:
        self._prev = square
