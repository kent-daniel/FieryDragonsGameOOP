import pygame
from GameConstants import GameStyles
from Player import Player


class Win:
    def __init__(self, player: Player, height: int = 200, width: int = 500,
                 colour=GameStyles.COLOR_GRAY_500.value):
        self.font = pygame.font.Font('freesansbold.ttf', 62)
        self.text = self.font.render(
            f'Congratulations Player {player.id}, YOU HAVE WON', True,
            (0, 0, 255), (255, 0, 0))
        self.textRect = self.text.get_rect()
        self.textRect.center = (600, 600)
        self.win_notif_surface: pygame.Surface = pygame.Surface(
            (width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.win_notif_surface, colour,
                         self.win_notif_surface.get_rect(),
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        self.rect: pygame.Rect = self.win_notif_surface.get_rect()

    def render_win(self, destination_surface, location):
        self.rect.center = location
        destination_surface.blit(self.win_notif_surface, self.rect.center)
        destination_surface.blit(self.text, self.rect.center)
