from typing import Tuple
from NotificationManager import NotificationManager
import pygame
from GameConstants import GameStyles

from Drawable import Drawable

class NotificationTabUI(Drawable):
    def __init__(self , height: int = 400 , width:int = 300, notification_manager = NotificationManager() , colour = GameStyles.COLOR_GRAY_500.value):
        self.notification_manager = notification_manager
        self.notification_surface: pygame.Surface = pygame.Surface((width, height), pygame.SRCALPHA)

        pygame.draw.rect(self.notification_surface, colour , self.notification_surface.get_rect() , border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
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
        font = pygame.font.SysFont(None, GameStyles.FONT_SIZE_SMALL.value)
        container_height = text_surface.get_height() + 10  # Height of each container
        y_offset = text_surface.get_height()  # Start drawing notifications below the title
        for notification in notifications:
            # Draw container rectangle
            container_rect = pygame.Rect(5, y_offset + 5, self.notification_surface.get_width() - 10, container_height)
            pygame.draw.rect(self.notification_surface, GameStyles.COLOR_GRAY_300.value, container_rect)
            pygame.draw.rect(self.notification_surface, GameStyles.COLOR_BLACK.value, container_rect, 2)  # Border

            # Render notification text
            text_surface = font.render(notification, True, GameStyles.COLOR_BLACK.value)
            text_rect = text_surface.get_rect(topleft=(15, y_offset + 10))  # Adjust x-position to create padding
            self.notification_surface.blit(text_surface, text_rect)

            y_offset += container_height + 5  #