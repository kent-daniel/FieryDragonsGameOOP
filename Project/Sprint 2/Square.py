from typing import Tuple
import pygame
import GameConstants

class Square(pygame.sprite.Sprite):
    def __init__(self, square_size: int, character: str) -> None:
        super().__init__()
        self._square_size: int = square_size
        self._character: str = character

        # can use flyweight factory
        self.image: pygame.Surface = pygame.image.load(character).convert_alpha()
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
    def character(self) -> str:
        return self._character

    @property
    def square_size(self) -> int:
        return self._square_size