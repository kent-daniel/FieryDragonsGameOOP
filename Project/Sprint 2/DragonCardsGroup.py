from typing import List, Tuple, Optional

import pygame

from GameConstants import GameImage, GameStyles, GameElementStyles
from DragonCard import DragonCard
from GameDataController import IDragonCardDataController
from Drawable import Drawable
from MovementEventManager import IMovementEventListener
from Movement import Movement

class DragonCardsGroup(IMovementEventListener):

    def __init__(self, data_controller: IDragonCardDataController,
                 screen: pygame.Surface,
                 width: int = GameElementStyles.DRAGON_CARD_AREA_HEIGHT.value,
                 height: int = GameElementStyles.DRAGON_CARD_AREA_HEIGHT.value,
                 arena_image: str = GameImage.VOLCANO_ARENA.value):
        self._data_controller = data_controller
        self._dragon_cards = self._data_controller.get_dragon_cards()
        self._width = width
        self._height = height
        self._image: pygame.Surface = pygame.image.load(arena_image).convert_alpha()
        self._image = pygame.transform.smoothscale(self._image, (self._width, self._height))
        # self._surface: pygame.Surface = pygame.Surface((self._width, self._height), pygame.SRCALPHA) # TODO : try passing screen in the constructor so we dont need to create another surface on top of the screem
        self._surface = screen
        # pygame.draw.rect(self._surface,
        #                  GameStyles.COLOR_TRANSPARENT.value,
        #                  self._surface.get_rect(),
        #                  )

        # self._surface.blit(self._image, self._image.get_rect(
        #     center=self._surface.get_rect().center))
        # self._rect = self._surface.get_rect()
        # self.redraw_view()

    def draw_on_screen(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        # self._rect.center = location
        # destination_surface.blit(self._surface, self._rect.topleft)

        destination_surface.blit(self._image, self._image.get_rect(
             center=location))
        self._draw_dragon_cards(destination_surface)



    def get_clicked_card(self, mouse_pos: (int, int)) -> Optional[DragonCard]:
        # relative_mouse_pos = (mouse_pos[0] - self._rect.x, mouse_pos[1] - self._rect.y) #BUG: click detection bug (only detects click on the top left of the card)
        for i in range(len(self._dragon_cards)):
            card = self._dragon_cards[i]
            if card.is_clicked(mouse_pos):
                self._dragon_cards[i] = card
                return self._dragon_cards[i]
        return None

    def reset_cards(self) -> None:
        for i in range(len(self._dragon_cards)):
            self._dragon_cards[i] = self._dragon_cards[i].unflip()
        # self.redraw_view()

    # def redraw_view(self) -> None:
    #     self._draw_dragon_cards()

    def _draw_dragon_cards(self , destination_surface) -> None:
        if not self._dragon_cards:
            return
        gap = 5
        startx = self._width * 0.15
        starty = 0
        card_width = self._dragon_cards[0].get_surface().get_width() if self._dragon_cards else 0
        num_row_cards = int((self._width * 0.8) // card_width) if card_width > 0 else 1

        for i, card in enumerate(self._dragon_cards):
            if i % num_row_cards == 0:
                startx = self._width * 0.15  # Reset x-coordinate for new row
                starty += card.get_surface().get_height() + gap  # Move to next row

            card.draw(destination_surface, (startx, starty))

            startx += card_width + gap

    def get_surface(self) -> pygame.Surface:
        return self._surface

    def on_movement_event(self, movement: Movement) -> None:
        # self.reset_cards()
        pass