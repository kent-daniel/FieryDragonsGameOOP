from typing import Tuple
from NotificationManager import NotificationManager
import pygame
from GameConstants import GameStyles

from Drawable import Drawable


class NotificationTabUI(Drawable):
    def __init__(self, height: int = 400, width: int = 300, notification_manager=NotificationManager(),
                 colour=GameStyles.COLOR_GRAY_500.value):
        self.notification_manager = notification_manager
        self.notification_surface: pygame.Surface = pygame.Surface((width, height), pygame.SRCALPHA)

        pygame.draw.rect(self.notification_surface, colour, self.notification_surface.get_rect(),
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        self.rect: pygame.Rect = self.notification_surface.get_rect()
        self.redraw_view()

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self.redraw_view()
        self.rect.topleft = location
        destination_surface.blit(self.notification_surface, self.rect.topleft)

    def get_surface(self) -> pygame.Surface:
        pass

    def redraw_view(self) -> None:
        self.notification_surface.fill(GameStyles.COLOR_GRAY_500.value)
        font = pygame.font.SysFont(None, GameStyles.FONT_SIZE_LARGE.value)
        text_surface = font.render("Notifications", True, GameStyles.COLOR_BLACK.value)
        self.notification_surface.blit(text_surface, text_surface.get_rect().topleft)

        notifications = self.notification_manager.notifications
        y_offset = text_surface.get_height() + 20  # Start drawing notifications below the title
        for notification in notifications:
            notification_item = NotificationItem(notification, self.notification_surface.get_width() - 20,
                                                 y_offset)
            notification_item.draw(self.notification_surface, (5, y_offset))
            y_offset += notification_item.surface.get_height() + 5  # spacing between notifications


class NotificationItem(Drawable):

    def __init__(self, message: str, surface_width: int, y_offset: int,
                 font_size: int = GameStyles.FONT_SIZE_MEDIUM.value, colour=GameStyles.COLOR_GRAY_300.value):
        self.surface = pygame.Surface((surface_width, font_size + 20), pygame.SRCALPHA)
        pygame.draw.rect(self.surface, colour, self.surface.get_rect(),
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        pygame.draw.rect(self.surface, GameStyles.COLOR_BLACK.value, self.surface.get_rect(), 2,
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)  # Border

        font = pygame.font.SysFont(None, font_size)
        text_surface = font.render(message, True, GameStyles.COLOR_BLACK.value)
        text_rect = text_surface.get_rect(center=(self.surface.get_width() // 2, self.surface.get_height() // 2))
        self.surface.blit(text_surface, text_rect)
        self.rect = self.surface.get_rect(topleft=(5, y_offset))

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self.rect.topleft = location
        destination_surface.blit(self.surface, self.rect.topleft)

    def get_surface(self) -> pygame.Surface:
        return self.surface

    def redraw_view(self) -> None:
        pass
