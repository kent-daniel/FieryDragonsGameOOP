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
    @abstractmethod
    def get_players(self) -> deque[Player]:
        pass

    @abstractmethod
    def set_players(self, players: deque[Player]) -> None:
        pass

    @abstractmethod
    def get_num_volcanoes(self) -> int:
        pass

    @abstractmethod
    def get_squares(self) -> List[Square]:
        pass

    @abstractmethod
    def set_squares(self, squares: List[Square]) -> None:
        pass


class PlayerDataController(IPlayerDataController):
    def __init__(self, squares_config_data: str, players_config_data: str):
        self._squares_config_data = squares_config_data
        self._players_count = players_config_data
        self._players: deque[Player] = deque()
        self._squares: List[Square] = []
        self.load_data()

    def get_players(self) -> deque[Player]:
        return self._players

    def set_players(self, players: deque[Player]) -> None:
        self._players = players

    def get_num_volcanoes(self) -> int:
        return len(self._players) * 2

    def get_squares(self) -> List[Square]:
        return self._squares

    def set_squares(self, squares: List[Square]) -> None:
        self._squares = squares

    def _create_squares(self) -> None:
        squares_list = self._parse_squares()
        player_index = 0
        num_volcanoes = len(self._players) * 2
        volcano_size = len(squares_list) // num_volcanoes
        for i in range(num_volcanoes):
            start_index = i * volcano_size
            end_index = start_index + volcano_size
            card_squares = squares_list[start_index:end_index]
            if i % 2 == 0:
                central_square_index = len(card_squares) // 2
                card_squares[central_square_index].attach_cave(Cave(self._players[player_index]))
                card_squares[central_square_index].set_occupant(self._players[player_index])
                player_index += 1
            self._squares += card_squares

    def _create_players(self) -> None:
        """
        Create and initialize the players based on the provided player count and square list.

        Args:
            self (PlayerDataController): An instance of the PlayerDataController class.

        Returns:
            None: This method does not return any value.

        Raises:
            None: This method does not raise any exceptions.

        Notes:
            This method creates a specified number of players and initializes them with unique IDs,
            the total number of squares, and a random color.
        """
        player_count: int = int(self._players_count)
        for player_id in range(1, player_count + 1):
            self._players.append(Player(player_id, len(self._parse_squares()), pygame.Color(randint(50, 255),
                                                                                                randint(50, 255),
                                                                                                randint(50, 255))))


    def _parse_squares(self) -> List[Square]:
        square_animals: List[str] = [animal.strip(" ") for animal in
                                     self._squares_config_data.split(",")]
        squares_list = [Square(i, CharacterImage[square_animals[i]]) for i in range(len(square_animals))]
        for i in range(len(squares_list)):
            squares_list[i].next = squares_list[(i + 1) % len(squares_list)]
            squares_list[i].prev = squares_list[(i - 1) % len(squares_list)]
        return squares_list

    def load_data(self):
        self._create_players()
        self._parse_squares()
        self._create_squares()

