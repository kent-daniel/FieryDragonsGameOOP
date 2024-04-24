from typing import Tuple

import pygame.sprite
from Drawable import Drawable

class Player(Drawable):

    def __init__(self, id: int , colour: pygame.Color):
        self.colour = colour
        self.id = id

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        pass

    def get_surface(self) -> pygame.Surface:
        pass