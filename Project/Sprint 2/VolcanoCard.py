import math
from typing import Tuple, List

import pygame.sprite

from Square import Square
import GameConstants

class VolcanoCard(pygame.sprite.Sprite):
    def __init__(self, card_squares: List[Square], width: int, height:int , padding: int) -> None:
        super().__init__()
        self.width = width
        self.height = height + 80
        self.card_surface: pygame.Surface = pygame.Surface((width, height + 50), pygame.SRCALPHA)
        pygame.draw.rect(self.card_surface,
                         GameConstants.GameStyles.COLOR_RED.value,
                         self.card_surface.get_rect(),
                         border_radius=GameConstants.GameStyles.BORDER_RADIUS_SMALL.value)
        self.rect: pygame.Rect = self.card_surface.get_rect()
        self.card_squares: List[Square] = card_squares
        self._padding: int = padding
        self._square_height: int = 75
        self._draw_squares_on_card()

    @property
    def squares(self) -> List[Square]:
        return self.card_squares
    def _draw_squares_on_card(self) -> None:
        total_width = self._square_height * len(self.card_squares) + (len(self.card_squares) - 1) * self._padding
        start_x = self.rect.centerx - total_width / 2
        start_y = self.rect.centery - self._square_height / 2

        for index, square in enumerate(self.card_squares):
            x = start_x + index * (self._square_height + self._padding)
            y = start_y
            square.draw(self.card_surface, (x, y))  # Draw square on the card surface

    def rotate(self, angle_degrees: float) -> None:
        self.card_surface = pygame.transform.rotate(self.card_surface, angle_degrees-90)
        self.rect = self.card_surface.get_rect(center=self.rect.center)

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self.rect.center = location
        destination_surface.blit(self.card_surface, self.rect.topleft)
