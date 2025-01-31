from abc import abstractmethod, ABC

import pygame

from GameConstants import CharacterImage, GameElementStyles, GameStyles
from typing import Tuple, Optional
from Player import Player
from Drawable import Drawable


class Tile(Drawable, ABC):
    def __init__(self, index: int, character: CharacterImage, width: int, height: int, occupant: Optional[Player] = None) -> None:
        self._id = index
        self._character: CharacterImage = character
        self._next: Optional[Tile] = None
        self._prev: Optional[Tile] = None
        self._occupant: Optional[Player] = occupant
        self.width = width
        self.height = height

    def get_occupant(self) -> Player or None:
        return self._occupant

    def set_occupant(self, player: Player) -> None:
        self._occupant = player

    def remove_occupant(self) -> None:
        self._occupant = None

    @abstractmethod
    def is_cave(self) -> bool:
        pass

    @property
    def id(self) -> int:
        return self._id

    @property
    def character(self) -> CharacterImage:
        return self._character

    @property
    def next(self) -> 'Tile':
        return self._next

    @next.setter
    def next(self, tile: 'Tile') -> None:
        self._next = tile

    @property
    def prev(self) -> 'Tile':
        return self._prev

    @prev.setter
    def prev(self, tile: 'Tile') -> None:
        self._prev = tile

    @id.setter
    def id(self, value):
        self._id = value

    @character.setter
    def character(self, value):
        self._character = value
