from typing import Tuple
from PreviousGameManager import PreviousGameManager
import pygame
from GameConstants import GameStyles, GameElementStyles
from Drawable import Drawable
class PreviousGameUI(Drawable):
    def __init__(self, height=GameElementStyles.SCREEN_HEIGHT.value, width=GameElementStyles.SCREEN_WIDTH.value,
                 previous_game_manager=PreviousGameManager(),
                 colour=GameStyles.COLOR_BROWN_LIGHT.value):
        self.previous_game_surface = pygame.Surface((width, height),pygame.SRCALPHA)