from random import randint
from typing import Tuple, Dict

import pygame.sprite
from Drawable import Drawable
from GameConstants import GameStyles, GameElementStyles
from IDecodable import IDecodable


class Player(Drawable, IDecodable):
    """
    Author: Kent Daniel and Guntaj Singh
    """

    def __init__(self,
                 id: int,
                 steps_to_win: int,
                 lives: int,
                 colour: pygame.Color = GameStyles.COLOR_GRAY_700.value,
                 width: int = GameElementStyles.PLAYER_HEIGHT.value,
                 height: int = GameElementStyles.PLAYER_HEIGHT.value):
        self.colour = colour
        self.id = id
        self.lives = lives
        self.steps_to_win = steps_to_win
        self._player_surface: pygame.Surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self._rect = self._player_surface.get_rect()
        radius_outer = height // 2
        pygame.draw.circle(self._player_surface, GameStyles.COLOR_BLACK.value, self._rect.center, radius_outer, width=3)

        radius_inner = radius_outer - 3
        pygame.draw.circle(self._player_surface, self.colour, self._rect.center, radius_inner)

        font = pygame.font.Font(None, 24)
        text_surface = font.render(str(self.id), True, GameStyles.COLOR_BLACK.value)
        text_rect = text_surface.get_rect(center=self._rect.center)
        self._player_surface.blit(text_surface, text_rect)

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self._rect.midtop = location
        destination_surface.blit(self._player_surface, self._rect.bottomleft)

    def get_surface(self) -> pygame.Surface:
        return self._player_surface

    def redraw_view(self) -> None:
        pass

    @staticmethod
    def decode_from_json(json_data: Dict) -> 'IDecodable':
        return Player(json_data["id"], json_data["steps_to_win"], json_data["lives"], pygame.Color(randint(50, 255),
                                                                               randint(50, 255),
                                                                               randint(50, 255)))

    def encode_to_json(self) -> Dict:
        return {"id": self.id, "steps_to_win": self.steps_to_win , "lives": self.lives}
