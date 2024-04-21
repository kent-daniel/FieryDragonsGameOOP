from typing import Tuple
import pygame
import GameConstants
from GameConstants import CharacterImage

class Square(pygame.sprite.Sprite):
    def __init__(self, square_size: int, character: CharacterImage) -> None:
        super().__init__()
        self._character: CharacterImage = character
        self._next: Square or None = None
        self._prev: Square or None = None

        # can use flyweight factory
        self.image: pygame.Surface = pygame.image.load(character.value).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (square_size*0.8, square_size*0.8))

        self.surface: pygame.Surface = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
        pygame.draw.rect(self.surface,
                         GameConstants.GameStyles.COLOR_BROWN.value ,
                         self.surface.get_rect(),
                         border_radius=GameConstants.GameStyles.BORDER_RADIUS_MEDIUM.value
                         )
        self.surface.blit(self.image, self.image.get_rect(center=(square_size//2, square_size//2)))
        self.rect: pygame.Rect = self.surface.get_rect()

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self.rect.topleft = location
        destination_surface.blit(self.surface, self.rect.topleft)

    @property
    def character(self) -> CharacterImage:
        return self._character

    @property
    def next(self) -> 'Square' or None:
        return self._next

    @next.setter
    def next(self, square: 'Square' or None) -> None:
        self._next = square

    @property
    def prev(self) -> 'Square' or None:
        return self._prev

    @prev.setter
    def prev(self, square: 'Square' or None) -> None:
        self._prev = square