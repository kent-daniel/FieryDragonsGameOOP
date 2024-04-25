import math
from typing import List, Tuple

import pygame.sprite
from VolcanoCard import VolcanoCard
from GameConstants import GameStyles, GameElementStyles
from GameDataController import GameDataController
from Drawable import Drawable


class Board(Drawable):
    def __init__(self, width: int, height: int, data_controller: GameDataController,
                 color: pygame.color = GameStyles.COLOR_TRANSPARENT.value):
        super().__init__()
        self.width = width
        self.height = height
        self.volcano_cards: List[VolcanoCard] = data_controller.volcano_cards
        self.board_surface: pygame.Surface = pygame.Surface((width, height), pygame.SRCALPHA)

        pygame.draw.rect(self.board_surface, color, self.board_surface.get_rect())
        self.rect: pygame.Rect = self.board_surface.get_rect()
        self._draw_volcano_cards()

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self.rect.center = location
        destination_surface.blit(self.board_surface, self.rect.topleft)

    def get_surface(self) -> pygame.Surface:
        return self.board_surface

    def _get_optimal_volcano_width(self, apothem: int, central_angle: float) -> int:
        central_angle_rad = math.radians(central_angle)
        # Calculate the minimum side length using the apothem length (using board radius) and central angle
        side_length = 2 * apothem * math.tan(central_angle_rad / 2)
        return int(side_length)

    def _draw_volcano_cards(self) -> None:
        apothem = self.width * 0.5 - 2 * GameElementStyles.SQUARE_LENGTH.value - GameStyles.PADDING_MEDIUM.value
        central_angle = 360 / len(self.volcano_cards)
        optimal_volcano_width = self._get_optimal_volcano_width(apothem,central_angle)
        rotation_degrees = 0
        for volcano in self.volcano_cards:
            volcano.set_optimal_width(optimal_volcano_width)
            volcano.rotate(rotation_degrees)
            # Calculate card center coordinate based on screen center and apothem
            volcano_card_center = (
                int(self.board_surface.get_rect().centerx + apothem * math.cos(math.radians(rotation_degrees))),
                int(self.board_surface.get_rect().centery - apothem * math.sin(math.radians(rotation_degrees)))
            )
            volcano.draw(self.board_surface, volcano_card_center)
            rotation_degrees += central_angle
