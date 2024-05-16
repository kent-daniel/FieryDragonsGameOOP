import pygame
from GameConstants import GameStyles
from Player import Player


class Win:
    def __init__(self, player: Player, colour=GameStyles.COLOR_GRAY_700_T.value):
        """

        :param player:
        :param colour:
        This initialises the constants of the win notification such as a surface for the notification to show on,
        and the text size,font and color
        """
        self.font = pygame.font.Font(GameStyles.FONT_WIN.value, GameStyles.FONT_SIZE_WIN.value)
        self.screen_width, self.screen_height = \
            pygame.display.get_desktop_sizes()[0]
        self.text = self.font.render(
            f'Congratulations Player {player.id}, YOU HAVE WON', True,
            GameStyles.COLOR_ORANGE.value, GameStyles.COLOR_BROWN_LIGHT.value)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.screen_width / 2, self.screen_height / 2)
        self.win_notif_surface: pygame.Surface = pygame.Surface(
            (self.screen_width, self.screen_height), pygame.SRCALPHA)
        pygame.draw.rect(self.win_notif_surface, colour,
                         self.win_notif_surface.get_rect(),
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        self.rect: pygame.Rect = self.win_notif_surface.get_rect()

    def render_win(self, destination_surface, location):
        """

        :param destination_surface:
        :param location:
        :return: The win notification on the GUI

        renders the surface on to the main screen then the text is rendered onto the surface
        """
        self.win_notif_surface.blit(self.text,
                                    self.textRect)
        destination_surface.blit(self.win_notif_surface, location)
