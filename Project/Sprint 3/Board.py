import math
from typing import List, Tuple
import pygame
from VolcanoCard import VolcanoCard
from GameConstants import GameStyles, GameElementStyles
from GameDataController import IPlayerDataController
from Drawable import Drawable
from MovementEventManager import IMovementEventListener
from Movement import Movement

#Garv Vohra
class Board(Drawable, IMovementEventListener):
    def __init__(self, width: int, height: int, data_controller: IPlayerDataController,
                 color: pygame.color = GameStyles.COLOR_TRANSPARENT.value):
        super().__init__()
        self.width = width
        self.height = height
        self._data_controller = data_controller
        self.volcano_cards: List[VolcanoCard] = []
        self.board_surface: pygame.Surface = pygame.Surface((width, height), pygame.SRCALPHA)

        pygame.draw.rect(self.board_surface, color, self.board_surface.get_rect())
        self.rect: pygame.Rect = self.board_surface.get_rect()
        self.redraw_view()

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

    def redraw_view(self) -> None:
        self._arrange_volcano_cards()
        self._draw_volcano_cards()

    def on_movement_event(self, movement: Movement) -> None:
        self.redraw_view()

    def _arrange_volcano_cards(self) -> None:
        squares = self._data_controller.get_squares()
        num_volcanoes = self._data_controller.get_num_volcanoes()
        num_squares_per_volcano = len(squares) // num_volcanoes
        volcano_cards = []
        for i in range(0, len(squares), num_squares_per_volcano):
            card_squares = squares[i:i + num_squares_per_volcano]
            volcano_card = VolcanoCard(card_squares)
            volcano_cards.append(volcano_card)
        self.volcano_cards = volcano_cards

    def _draw_volcano_cards(self) -> None:
        apothem = self.width * 0.50 - 2 * GameElementStyles.SQUARE_LENGTH.value - GameStyles.PADDING_MEDIUM.value
        central_angle = 360 / len(self.volcano_cards)
        optimal_volcano_width = self._get_optimal_volcano_width(apothem, central_angle)
        rotation_degrees = 0
        for volcano in self.volcano_cards:
            volcano.set_optimal_width(optimal_volcano_width)
            volcano.rotate(rotation_degrees)
            # Calculate card center coordinate based on screen center and apothem https://en.wikipedia.org/wiki/Apothem
            volcano_card_center = (
                int(self.board_surface.get_rect().centerx + apothem * math.cos(math.radians(rotation_degrees))),
                int(self.board_surface.get_rect().centery - apothem * math.sin(math.radians(rotation_degrees)))
            )
            volcano.draw(self.board_surface, volcano_card_center)
            rotation_degrees -= central_angle
