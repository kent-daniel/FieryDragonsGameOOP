import math
from typing import Tuple, List

import pygame.sprite

from Square import Square
import GameConstants

class VolcanoCard(pygame.sprite.Sprite):
    def __init__(self, card_squares: List[Square], width: int, height: int) -> None:
        super().__init__()
        self.card_surface: pygame.Surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.card_surface,
                         GameConstants.GameStyles.COLOR_BROWN.value,
                         self.card_surface.get_rect(),
                         border_radius=GameConstants.GameStyles.BORDER_RADIUS_SMALL.value)
        self.rect: pygame.Rect = self.card_surface.get_rect()
        self._squares: List[Square] = card_squares
        self._draw_squares_on_card()

    @property
    def squares(self) -> List[Square]:
        return self._squares
    def _draw_squares_on_card(self, gutter_width:int = 10) -> None:

        total_width = sum(square.square_size for square in self._squares) + (len(self._squares) - 1) * gutter_width

        start_x = self.rect.centerx - total_width / 2
        start_y = self.rect.centery - self._squares[0].square_size / 2

        for index, square in enumerate(self._squares):
            x = start_x + index * (square.square_size + gutter_width)
            y = start_y
            square.draw(self.card_surface, (x, y))  # Draw square on the card surface

    def rotate(self, angle_degrees: float, central_angle:int,  rotation_center: Tuple[int, int]) -> None:
        """Rotate the card around the specified rotation center."""
        # screen_center = rotation_center
        # apothem = self._calculate_minimum_distance_from_center(self.card_surface.get_width(), central_angle)
        #
        # # Calculate card center coordinate based on screen center and apothem
        # center = (
        #     int(screen_center[0] + apothem * math.cos(math.radians(angle_degrees))),
        #     int(screen_center[1] - apothem * math.sin(math.radians(angle_degrees)))
        # )

        self.card_surface = pygame.transform.rotate(self.card_surface, angle_degrees - 90)
        self.rect = self.card_surface.get_rect(center=self.rect.center)

        # # Calculate offset from current center to the new rotation center
        # offset_x = center[0] - self.rect.centerx
        # offset_y = center[1] - self.rect.centery
        #
        # # Adjust rectangle position based on the offset
        # self.rect.centerx += offset_x
        # self.rect.centery += offset_y

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self.rect.center = location
        destination_surface.blit(self.card_surface, self.rect.topleft)

    def _calculate_minimum_distance_from_center(self,side_length: float, angle: float) -> float:
        central_angle_rad = math.radians(angle)
        # Calculate the apothem using the trigonometric relationship https://en.wikipedia.org/wiki/Apothem
        apothem_length = side_length / (2 * math.tan(central_angle_rad / 2))
        print(apothem_length)
        return apothem_length