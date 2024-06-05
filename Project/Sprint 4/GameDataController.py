import json
import os
import sys
from collections import OrderedDict
from datetime import datetime
from typing import List
from PlayerDataController import IPlayerDataController, PlayerDataController
from DragonCardDataController import IDragonCardDataController, DragonCardDataController
from LocationDataController import ILocationDataController, LocationDataController
from LocationManager import LocationManager


class GameProgressData:
    def __init__(self, jsonData, timestamp):
        self.time_saved = timestamp
        self.player_info = self.parse_players_info(jsonData["players_info"])
        self.caves = self.parse_caves(jsonData["caves"])
        self.squares = self.parse_squares(jsonData["squares"])
        self.dragon_cards = self.parse_dragon_cards(jsonData["dragon_cards"])

    def parse_players_info(self, players_info):
        return [
            {
                "id": player["id"],
                "steps_to_win": player["steps_to_win"]
            }
            for player in players_info
        ]

    def parse_caves(self, caves):
        return [
            {
                "animal": cave["animal"],
                "position": cave["position"],
                "owner": cave['owner'],
                "occupant": cave['occupant']
            }
            for cave in caves
        ]

    def parse_squares(self, tiles):
        return [
            {
                "occupant": tile["occupant"],
                "animal": tile["animal"]
            }
            for tile in tiles
        ]

    def parse_dragon_cards(self, dragon_cards):
        return [
            {
                "value": card["value"],
                "character": card["character"]
            }
            for card in dragon_cards
        ]


class GameDataController:
    def __init__(self, config_path: str = 'config.json'):
        self.location_manager = None
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

        # Prepare new game data
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        players_info = self.player_data_controller.to_json_format()
        squares_data = self.location_data_controller.to_json_format_square()
        caves_data = self.location_data_controller.to_json_format_cave()
        dragon_cards = self.dragon_card_data_controller.to_json_format()

        # Add new game data
        new_game_data = {
            timestamp: {
                "players_info": players_info,
                "caves": caves_data,
                "squares": squares_data,
                "dragon_cards": dragon_cards
            }
        }
        print(new_game_data)
        data.update(new_game_data)

        # Write the updated data back to the JSON file
        with open(file_path, 'w') as file:
            json.dump(OrderedDict(sorted(data.items())), file, indent=4)

    def load_from_game(self, game_data: GameProgressData):
        print(game_data.caves)
        self.player_data_controller = PlayerDataController(game_data.player_info)
        self.dragon_card_data_controller = DragonCardDataController(game_data.dragon_cards)
        self.location_data_controller = LocationDataController(game_data.squares,
                                                               game_data.caves,
                                                               self.player_data_controller.get_players())
        self.location_manager = LocationManager(self.location_data_controller, self.player_data_controller)

    def load_from_new_game(self, num_players: int):
        default_config = self._parse_config('config.default.json')
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        default_game = GameProgressData(default_config["default"], current_time)
        default_game.player_info = default_game.player_info[:num_players]
        cave_spacing = 24 // num_players
        # Initialize position of the caves
        caves = []
        position = 1
        for cave in default_game.caves:
            cave["position"] = position
            caves.append(cave)
            position += cave_spacing
        default_game.caves = caves[:num_players]
        self.load_from_game(default_game)

    def to_json(self, players, caves, squares, dragon_cards) -> dict:
        players_info = [
            {'id': player.id,
             'steps_to_win': player.steps_to_win
             } for player in players]
        caves_info = [
            {'animal': cave.character.name,
             'position': cave.id,
             'owner': cave.get_owner().id,
             'occupant': cave.get_owner().id if cave.get_occupant() else None
             } for cave in caves]
        squares_info = [
            {'animal': square.character.name,
             'occupant': square.get_occupant().id if square.get_occupant() else None
             } for square in squares]
        dragon_cards_info = [
            {'value': card.value,
             'character': card.character.name}
            for card in dragon_cards]

        return {
            'players_info': players_info,
            'caves': caves_info,
            'squares': squares_info,
            'dragon_cards': dragon_cards_info
        }

    def get_saved_games(self) -> List[GameProgressData]:
        return self.game_progress_list
