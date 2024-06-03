from typing import Tuple
from PreviousGameManager import PreviousGameManager
import pygame
from GameConstants import GameStyles, GameElementStyles
from Drawable import Drawable


class PreviousGameUI(Drawable):
    def __init__(self, height=GameElementStyles.SCREEN_HEIGHT.value, width=GameElementStyles.SCREEN_WIDTH.value,
                 previous_game_manager=PreviousGameManager(),
                 colour=GameStyles.COLOR_BROWN_LIGHT.value):
        self.previous_game_manager = previous_game_manager
        self.previous_game_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.previous_game_surface, colour, self.previous_game_surface.get_rect())
        self.rect: pygame.Rect = self.previous_game_surface.get_rect()
        self.redraw_view()

    def draw(self, destination_surface: pygame.Surface, location:Tuple[int, int] =GameElementStyles.TOP_LEFT.value) -> None:
        self.redraw_view()
        self.rect.topleft = location
        destination_surface.blit(self.previous_game_surface, self.rect.topleft)
    def get_surface(self) -> pygame.Surface:
        pass

    def redraw_view(self) -> None:
        pass

class PreviousGameItem(Drawable):
    def __init__(self, height=GameElementStyles.SCREEN_HEIGHT.value, width=GameElementStyles.SCREEN_WIDTH.value,
                 previous_game_manager=PreviousGameManager(),
                 colour=GameStyles.COLOR_BROWN_LIGHT.value):

