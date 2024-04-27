from typing import Tuple, List

import pygame.sprite

from Square import Square
from GameConstants import GameElementStyles, GameStyles


class VolcanoCard(pygame.sprite.Sprite):
    def __init__(self, card_squares: List[Square], width: int = 0, height: int = GameElementStyles.SQUARE_LENGTH.value,
                 paddingx: int = GameStyles.PADDING_SMALL.value,
                 paddingy: int = GameStyles.PADDING_LARGE.value) -> None:
        super().__init__()
        self.width = width
        self.height = height + 2 * paddingy
        self.card_squares: List[Square] = card_squares
        self._square_gap: int = paddingx
        self.card_surface: pygame.Surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self._draw_surface()

    @property
    def squares(self) -> List[Square]:
        return self.card_squares
    @squares.setter
    def squares(self, squares: List[Square]) -> None:
        self.card_squares = squares

    def _draw_surface(self):
        pygame.draw.rect(self.card_surface,
                         GameStyles.COLOR_BROWN_DARK.value,
                         self.card_surface.get_rect(),
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        self.rect: pygame.Rect = self.card_surface.get_rect()
        self._draw_squares_on_card()

    def set_optimal_width(self, optimal_width: int):
        self.card_surface: pygame.Surface = pygame.Surface((optimal_width + self._square_gap*2, self.height), pygame.SRCALPHA)
        self._draw_surface()

    def _draw_squares_on_card(self) -> None:
        total_width = GameElementStyles.SQUARE_LENGTH.value * len(self.card_squares) + (
                    len(self.card_squares) - 1) * self._square_gap
        start_x = self.rect.centerx - total_width / 2
        start_y = self.rect.centery - GameElementStyles.SQUARE_LENGTH.value / 2

        for index, square in enumerate(self.card_squares):
            x = start_x + index * (GameElementStyles.SQUARE_LENGTH.value + self._square_gap)
            y = start_y

            square.redraw_view()
            square.draw(self.card_surface, (x, y))

    def rotate(self, angle_degrees: float) -> None:
        self.card_surface = pygame.transform.rotate(self.card_surface, angle_degrees - 90)
        self.rect = self.card_surface.get_rect(center=self.rect.center)

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self.rect.center = location
        destination_surface.blit(self.card_surface, self.rect.topleft)
