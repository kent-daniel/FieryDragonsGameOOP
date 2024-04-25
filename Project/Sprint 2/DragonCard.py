from abc import ABC, abstractmethod
from typing import Tuple
from Square import Square
import pygame
from GameConstants import CharacterImage
from Drawable import Drawable
from GameConstants import GameStyles
from Movement import Movement


class DragonCard(Drawable, ABC):
    def __init__(self, character: CharacterImage, value: int, is_flipped: bool = False, radius: int = 45):
        self._character = character
        self._value = value
        self._character = character
        self._radius = radius
        self._is_flipped = is_flipped
        self._image: pygame.Surface = pygame.image.load(self._character.value).convert_alpha()
        self._image = pygame.transform.smoothscale(self._image, (self._radius * 0.8, self._radius * 0.8))
        self._surface: pygame.Surface = pygame.Surface((self._radius * 2, self._radius * 2), pygame.SRCALPHA)
        self._rect: pygame.Rect = self._surface.get_rect()
        self._render_card()

    def unflip(self):
        self._is_flipped = False

    def is_clicked(self, mouse_pos: Tuple[int, int]) -> bool:
        print((self._rect.left+self._rect.width , self._rect.top+self._rect.width)  , mouse_pos)
        if self._rect.collidepoint(mouse_pos):
            self._is_flipped = True
            return True
        return False

    def _render_card(self):
        self._surface.fill(GameStyles.COLOR_TRANSPARENT.value)
        if self._is_flipped:
            self._surface.blit(self._image, self._image.get_rect(center=self._surface.get_rect().center))
            pygame.draw.circle(self._surface, GameStyles.COLOR_PINK.value, (self._radius, self._radius), self._radius)
        else:
            pygame.draw.circle(self._surface, GameStyles.COLOR_PINK.value, (self._radius, self._radius), self._radius)

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self._rect.center = location
        destination_surface.blit(self._surface,self._rect.center)

    def get_surface(self) -> pygame.Surface:
        return self._surface

    @property
    def character(self) -> CharacterImage:
        return self._character

    @property
    def value(self) -> int:
        return self._value

    @abstractmethod
    def action(self, square: Square) -> Movement:
        pass


class AnimalDragonCard(DragonCard):
    def __init__(self, character: CharacterImage, value: int, is_flipped: bool = False, radius: int = 30):
        super().__init__(character, value, is_flipped)

    def action(self, square: Square) -> Movement:
        if square.character != self.character:
            return Movement(0, square)
        destination = square
        for i in range(self.value):
            destination = destination.next

        return Movement(self.value, destination)


class PirateDragonCard(DragonCard):
    def __init__(self, character: CharacterImage, value: int, is_flipped: bool = False, radius: int = 30):
        super().__init__(character, value, is_flipped)

    def action(self, square: Square) -> Movement:
        destination = square
        for i in range(self.value):
            destination = destination.prev
        return Movement(-self.value, destination)
