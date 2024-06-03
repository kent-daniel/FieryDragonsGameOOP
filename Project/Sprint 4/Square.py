from typing import Tuple, Optional
import pygame
from GameConstants import CharacterImage, GameElementStyles, GameStyles
from Drawable import Drawable
from Player import Player
from Cave import Cave
from Tile import Tile


class Square(Tile):
    def __init__(self, id: int, character: CharacterImage,
                 width: int = GameElementStyles.SQUARE_LENGTH.value,
                 height: int = GameElementStyles.SQUARE_LENGTH.value) -> None:
        super().__init__(id, character, width, height)
        self._cave: Optional[Cave] = None
        self._rect = None
        self._image: pygame.Surface = pygame.image.load(self._character.value).convert_alpha()
        self._image = pygame.transform.smoothscale(self._image, (self.width * 0.8, self.height * 0.8))
        self._square_surface: pygame.Surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self._combined_surface: pygame.Surface = self._square_surface
        self.redraw_view()

    def redraw_view(self) -> None:
        self._rect: pygame.Rect = self._combined_surface.get_rect()
        self._draw_square()
        self._draw_cave()
        if self._occupant:
            self._draw_player()

    @property
    def cave(self) -> Optional[Cave]:
        return self._cave

    def _draw_square(self) -> None:
        square_colour = self._occupant.colour if self._occupant is not None else GameStyles.COLOR_BROWN_LIGHT.value
        pygame.draw.rect(self._square_surface,
                         square_colour,
                         self._square_surface.get_rect(),
                         border_radius=GameStyles.BORDER_RADIUS_MEDIUM.value
                         )

        self._square_surface.blit(self._image, self._image.get_rect(
            center=(self._square_surface.get_width() // 2, self._square_surface.get_height() // 2)))
        self._combined_surface.blit(self._square_surface, self._rect.topleft)

    def _draw_cave(self) -> None:
        if self._cave is None: return
        self._cave.draw(self._combined_surface,
                        (self._rect.centerx, self._rect.centery + GameElementStyles.CAVE_OFFSET.value))

    def _draw_player(self) -> None:
        if self._occupant is None: return
        self._occupant.draw(self._combined_surface, self._rect.midtop)

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self._rect.topleft = location
        destination_surface.blit(self._combined_surface, self._rect.topleft)

    def get_surface(self) -> pygame.Surface:
        return self._combined_surface

    def attach_cave(self, cave: Cave) -> None:
        self._combined_surface = pygame.Surface(
            (self.width, self.height + cave.get_surface().get_rect().height), pygame.SRCALPHA)
        self._cave = cave
