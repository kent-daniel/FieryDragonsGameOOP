import json
import os
import random
import sys
from collections import OrderedDict
from datetime import datetime
from typing import List, Callable
from PlayerDataController import IPlayerDataController, PlayerDataController
from DragonCardDataController import IDragonCardDataController, DragonCardDataController
from LocationDataController import ILocationDataController, LocationDataController
from Player import Player
from Square import Square
from Cave import Cave
from DragonCard import DragonCard
from IDecodable import IDecodable
from GameConstants import CharacterImage


class GameProgressData:
    def __init__(self, json_data, timestamp):
        self.time_saved = timestamp
        self.players = self._decode_from_json(json_data["players_info"], Player.decode_from_json)
        self.squares = self._decode_from_json(json_data["squares"], Square.decode_from_json)
        self.dragon_cards = self._decode_from_json(json_data["dragon_cards"], DragonCard.decode_from_json)

    def _decode_from_json(self, json_list: list[dict], decoder: Callable) -> List[IDecodable]:
        return [decoder(data) for data in json_list]


class GameDataController:
    def __init__(self, config_path: str = 'config.json'):
        self.config = self._parse_config(config_path)
        self.game_progress_list: List[GameProgressData] = [GameProgressData(self.config[timestamp], timestamp) for
                                                           timestamp in self.config]
        self.player_data_controller: IPlayerDataController = None
        self.dragon_card_data_controller: IDragonCardDataController = None
        self.location_data_controller: ILocationDataController = None

    def _parse_config(self, config_path: str) -> dict:
        filepath = self.resource_path(config_path)
        with open(filepath, 'r') as config_file:
            config = json.load(config_file)
        return config

    def resource_path(self, relative_path: str):
        """ Get absolute path to resource, works for dev and for PyInstaller """

        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def save_data(self):
        # Read existing data from the JSON file
        file_path = self.resource_path('config.json')
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Check the number of saved games
        if len(data) >= 3:
            # Remove the oldest game data
            oldest_game = sorted(data.keys())[0]
            del data[oldest_game]

        # Add new game data
        game_data = self.get_current_game_json()
        data.update(game_data)

        # Write the updated data back to the JSON file
        with open(file_path, 'w') as file:
            json.dump(OrderedDict(sorted(data.items())), file, indent=4)

    def load_from_game(self, game_data: GameProgressData):
        self.player_data_controller = PlayerDataController(game_data.players)
        self.dragon_card_data_controller = DragonCardDataController(game_data.dragon_cards)
        self.location_data_controller = LocationDataController(game_data.squares,
                                                               self.player_data_controller.get_players())

    def load_from_new_game(self, num_players: int):
        default_config = self._parse_config('config.default.json')
        cave_spacing = 24 // num_players
        # Initialize position of the caves
        default_game_caves = default_config["default"]["caves"][:num_players]
        position = 1
        for cave in default_game_caves:
            default_config["default"]["squares"][position]["cave"] = cave
            position += cave_spacing
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        default_game = GameProgressData(default_config["default"], current_time)
        default_game.players = default_game.players[:num_players]
        self.load_from_game(default_game)

    def get_current_game_json(self) -> dict:
        # Prepare new game data
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        players_info = self.player_data_controller.to_json_format()
        squares_data = self.location_data_controller.to_json_format_square()
        dragon_cards = self.dragon_card_data_controller.to_json_format()

        return {
            timestamp: {
                "players_info": players_info,
                "squares": squares_data,
                "dragon_cards": dragon_cards
            }
        }

    def get_saved_games(self) -> List[GameProgressData]:
        return self.game_progress_list
