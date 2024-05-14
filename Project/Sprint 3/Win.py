import pygame
from GameConstants import GameStyles
from Player import Player


class Win:
    def __init__(self, player: Player, colour=(50, 50, 50, 190)): #todo add color to gamestyles
        self.font = pygame.font.Font('freesansbold.ttf', 62) #todo correct the font
        self.screen_width, self.screen_height = \
            pygame.display.get_desktop_sizes()[0]
        self.text = self.font.render(
            f'Congratulations Player {player.id}, YOU HAVE WON', True,
            (0, 0, 255), (255, 0, 0)) #todo fix color and font
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.screen_width / 2, self.screen_height / 2)
        # self.textrect.center =
        self.win_notif_surface: pygame.Surface = pygame.Surface(
            (self.screen_width, self.screen_height), pygame.SRCALPHA)
        pygame.draw.rect(self.win_notif_surface, colour,
                         self.win_notif_surface.get_rect(),
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        self.rect: pygame.Rect = self.win_notif_surface.get_rect()

    def render_win(self, destination_surface, location):
        self.win_notif_surface.blit(self.text,
                                    self.textRect)
        destination_surface.blit(self.win_notif_surface, location)
