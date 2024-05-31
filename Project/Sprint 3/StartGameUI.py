from typing import Tuple
import pygame
from GameConstants import GameStyles, GameElementStyles

from Drawable import Drawable


class StartGameUI(Drawable):

    def __init__(self, height=GameElementStyles.SCREEN_HEIGHT.value, width=GameElementStyles.SCREEN_WIDTH.value,
                 button_height=GameElementStyles.BUTTON_HEIGHT.value, button_width=GameElementStyles.BUTTON_WIDTH.value,
                 spacing=GameElementStyles.SPACING.value, surface_colour=GameStyles.COLOR_BROWN_LIGHT.value,
                 button_colour=GameElementStyles.COLOR_BROWN_DARK.value):
        self.start_game_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.new_game_rect = pygame.Rect(width // 2 - button_width // 2, height // 2 - button_height - spacing // 2,
                                         button_width, button_height)
        self.previous_game_rect = pygame.Rect(width // 2 - button_width // 2, height // 2 + spacing // 2, button_width,
                                              button_height)
        pygame.draw.rect(self.start_game_surface, surface_colour, self.start_game_surface.get_rect())
        pygame.draw.rect(self.start_game_surface, button_colour,
                         self.new_game_rect,
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        pygame.draw.rect(self.start_game_surface, button_colour, self.previous_game_rect,
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        self.rect: pygame.Rect = self.start_game_surface.get_rect()

        self.redraw_view()

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self.redraw_view()
        self.rect.topleft = GameElementStyles.TOP_LEFT.value
        destination_surface.blit(self.start_game_surface, self.rect.topleft)

    def get_surface(self) -> pygame.Surface:
        pass

    def redraw_view(self) -> None:
        font = pygame.font.SysFont(None, GameStyles.FONT_SIZE_LARGE.value)
        new_game_text = font.render("New Game", True, GameStyles.COLOR_BLACK.value)
        previous_game_text = font.render("Previous Game", True, GameStyles.COLOR_BLACK.value)
        self.start_game_surface.blit(new_game_text, new_game_text.get_rect(center=self.new_game_rect.center))
        self.start_game_surface.blit(previous_game_text,
                                     previous_game_text.get_rect(center=self.previous_game_rect.center))



