from typing import Tuple
import pygame
from GameConstants import GameStyles, GameElementStyles

from Drawable import Drawable


class StartGameUI(Drawable):

    def __init__(self, height=GameElementStyles.SCREEN_HEIGHT, width=GameElementStyles.SCREEN_WIDTH,
                 colour=GameStyles.COLOR_BROWN_LIGHT.value):
        self.Start_game_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.new_game_rect = (self.Start_game_surface, colour, pygame.Rect(0, 0, width, height),
                              GameStyles.BORDER_RADIUS_SMALL.value)

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        pass

    def get_surface(self) -> pygame.Surface:
        pass

    def redraw_view(self) -> None:
        pass
