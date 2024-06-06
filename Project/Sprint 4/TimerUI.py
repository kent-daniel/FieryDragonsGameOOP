from abc import ABC
from typing import Tuple
from TimerController import TimerController
from PlayerTurnController import PlayerTurnController
import pygame
from Drawable import Drawable
from GameConstants import GameStyles

class TimerUI(Drawable):
    def __init__(self, timer_controller: TimerController, width=150,
                 height=150, colour=GameStyles.COLOR_TRANSPARENT.value):
        self.text = None
        self.screen_width, self.screen_height = pygame.display.get_desktop_sizes()[0]
        self._timer_controller = timer_controller
        self.timer_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.location = pygame.Rect(self.screen_width-width, self.screen_height-height,width,height)
        pygame.draw.rect(self.timer_surface, colour,
                         self.location,
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        self.rect: pygame.Rect = self.timer_surface.get_rect()
        self.redraw_view()
        self.timer_emoji = " Timer: "
    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self.text = self.timer_emoji + self._timer_controller.get_time()
        self.redraw_view()
        destination_surface.blit(self.timer_surface, self.location.topleft)

    def get_surface(self):
        pass
    def redraw_view(self) -> None:
        font = pygame.font.SysFont(None, GameStyles.FONT_SIZE_LARGE.value)
        text_surface = font.render(self.text, True, GameStyles.COLOR_BROWN_DARK.value, GameStyles.COLOR_BROWN_LIGHT.value)
        self.timer_surface.blit(text_surface,(0,0,100,100))

