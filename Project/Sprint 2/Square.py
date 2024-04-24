from typing import Tuple, Optional
import pygame
from GameConstants import CharacterImage, GameElementStyles, GameStyles
from Drawable import Drawable
from Player import Player
from Cave import Cave


class Square(Drawable):
    def __init__(self, id: int, character: CharacterImage, width: int = GameElementStyles.SQUARE_LENGTH.value,
                 height: int = GameElementStyles.SQUARE_LENGTH.value) -> None:
        self._id = id
        self._character: CharacterImage = character
        self._next: Optional[Square] = None
        self._prev: Optional[Square] = None
        self._occupant: Optional[Player] = None
        self._cave: Optional[Cave] = None
        self._rect = None
        self._width = width
        self._height = height
        self._image: pygame.Surface = pygame.image.load(character.value).convert_alpha()
        self._image = pygame.transform.smoothscale(self._image, (width * 0.8, height * 0.8))

        self._surface: pygame.Surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self._update_square_drawing()

    def _update_square_drawing(self) -> None:
        self._surface.fill(GameStyles.COLOR_TRANSPARENT.value)
        pygame.draw.rect(self._surface,
                         GameStyles.COLOR_BROWN.value,
                         self._surface.get_rect(),
                         border_radius=GameStyles.BORDER_RADIUS_MEDIUM.value
                         )
        self._surface.blit(self._image, self._image.get_rect(center=(self._width // 2, self._height // 2)))
        self._rect: pygame.Rect = self._surface.get_rect()
        self._draw_player()
        self._draw_cave()

    def _draw_cave(self) -> None:
        if self._cave is None: return
        self._cave.draw(self._surface,self._rect.topleft)

    def _draw_player(self) -> None:
        if self._occupant is None: return
        self._occupant.draw(self._surface, self._rect.center)

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self._rect.topleft = location
        destination_surface.blit(self._surface, self._rect.topleft)

    def get_surface(self) -> pygame.Surface:
        return self._surface

    def get_occupant(self) -> Player or None:
        return self._occupant

    def accept_player(self, player: Player) -> None:
        self._occupant = player
        self._update_square_drawing()
    def remove_player(self) -> None:
        self._occupant = None
        self._update_square_drawing()
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
