from abc import ABC, abstractmethod
from typing import List
from Square import Square
from Cave import Cave
import pygame
from Player import Player
from GameConstants import CharacterImage
from collections import deque
from random import randint


class IPlayerDataController(ABC):
    """
    Author: Garv Vohra
    Interface for managing player data in the game.
    """

    @abstractmethod
    def get_players(self) -> deque[Player]:
        pass

    @abstractmethod
    def set_players(self, players: deque[Player]) -> None:
        pass

    @abstractmethod
    def to_json_format(self) -> List[dict]:
        pass


class PlayerDataController(IPlayerDataController):
    """
    Author: Garv Vohra
    Concrete implementation of IPlayerDataController to manage player and square data in the game.

    Attributes:
        _squares_config_data (str): Configuration data for squares.
        _players_count (str): Configuration data for the number of players.
        _players (deque[Player]): A deque of Player objects.
        _squares (List[Square]): A list of Square objects.
    """

    def __init__(self, players: List[Player]):
        self._players: deque[Player] = deque(players)

    def get_players(self) -> deque[Player]:
        return self._players

    def set_players(self, players: deque[Player]) -> None:
        self._players = players

    def to_json_format(self) -> List[dict]:
        return [player.encode_to_json() for player in self._players]
