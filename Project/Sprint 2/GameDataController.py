from collections import deque
from configparser import ConfigParser
from random import randint
from typing import List
import pygame
from VolcanoCard import VolcanoCard
from Player import Player
from DragonCard import DragonCard
from GameConstants import GameStyles, CharacterImage
from Square import Square
from Cave import Cave


class GameDataController:
    def __init__(self, config_path: str):
        self.config = ConfigParser()
        self.config.read(config_path)

        self.dragon_cards: List[DragonCard] = []
        self._volcano_cards: List[VolcanoCard] = []
        self.players: deque[Player] = deque()
        self.load_game_data()

    @property
    def volcano_cards(self):
        return self._volcano_cards

    def load_game_data(self):
        self._create_players()
        self._create_volcano_cards()

    def _create_players(self) -> None:
        player_count :int = int(self.config.get('GameConfig', 'player_count'))
        for player_id in range(1, player_count + 1):
            self.players.append(Player(player_id, pygame.Color((randint(0, 255), randint(0, 255), randint(0, 255)))))

    def _create_volcano_cards(self) -> None:
        squares_list = self._parse_squares()
        player_index = 0
        num_volcanoes = len(self.players) * 2
        volcano_size = len(squares_list) // num_volcanoes
        for i in range(num_volcanoes):
            start_index = i * volcano_size
            end_index = start_index + volcano_size
            card_squares = squares_list[start_index:end_index]
            if i % 2 == 0:
                central_square_index = len(card_squares) // 2
                card_squares[central_square_index].attach_cave(Cave(self.players[player_index]))
                card_squares[central_square_index].set_occupant(self.players[player_index])
                player_index += 1
            self._volcano_cards.append(VolcanoCard(card_squares))

    def _parse_squares(self) -> List[Square]:
        square_animals: List[str] = [animal.strip(" ") for animal in
                                     self.config.get('GameConfig', 'square_animals').split(",")]
        squares_list = [Square(i, CharacterImage[square_animals[i]]) for i in range(len(square_animals))]
        for i in range(len(squares_list)):
            squares_list[i].next = squares_list[(i + 1) % len(squares_list)]
            squares_list[i].prev = squares_list[(i - 1) % len(squares_list)]
        return squares_list

    def set_volcano_cards(self, value: List[VolcanoCard]):
        self._volcano_cards = value
