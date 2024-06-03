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

    def __init__(self, players_config_data: List[dict]):
        self._players_data = players_config_data
        self._players: deque[Player] = deque()
        self._squares: List[Square] = []
        self.load_data()

    def get_players(self) -> deque[Player]:
        return self._players

    def set_players(self, players: deque[Player]) -> None:
        self._players = players

    def _create_players(self) -> None:
        for player in self._players_data:
            self._players.append(Player(player["id"], player["steps_to_win"], pygame.Color(randint(50, 255),
                                                                                           randint(50, 255),
                                                                                           randint(50, 255))))

    def to_config_format(self) -> List[dict]:
        return [{"id": player.id , "steps_to_win": player.steps_to_win} for player in self._players]

    def load_data(self):
        self._create_players()
