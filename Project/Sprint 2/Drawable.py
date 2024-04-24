import pygame
from abc import ABC, abstractmethod
from typing import Tuple

class Drawable(ABC):
    @abstractmethod
    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        pass

    @abstractmethod
    def get_surface(self) -> pygame.Surface:
        pass
