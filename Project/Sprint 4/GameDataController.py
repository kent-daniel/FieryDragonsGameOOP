import json
import os
import sys
from typing import List

from PlayerDataController import IPlayerDataController, PlayerDataController
from DragonCardDataController import IDragonCardDataController, DragonCardDataController
from LocationDataController import ILocationDataController, LocationDataController


class GameProgressData:
    def __init__(self, data, timestamp):
        self.time_saved = timestamp
        self.player_info = self.parse_players_info(data["players_info"])
        self.caves = self.parse_caves(data["caves"])
        self.tiles = self.parse_tiles(data["tiles"])
        self.dragon_cards = self.parse_dragon_cards(data["dragon_cards"])

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
                "position": cave["position"],
                "owner": cave['owner']
            }
            for cave in caves
        ]

    def parse_tiles(self, tiles):
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
                "animal": card["animal"]
            }
            for card in dragon_cards
        ]


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
        pass
        #TODO if 3 games saved , only pick the last 2 games + new saved data
        # timestamp = Date()
        # self.player_data_controller.get_players_config_data()
        # self.dragon_card_data_controller.get_dragon_cards_config_data()
        # self.location_data_controller.get_squares_config_data()
        # self.location_data_controller.get_cave_config_data()
        # data = {
        #     players_info
        #     caves
        #     square_animals
        #     dragon_cards
        # }
        # modify / delete / create new file

    def load_from_saved_config(self, date: str):
        for game in self.game_progress_list:
            if game.time_saved == date:
                self.player_data_controller = PlayerDataController(game.player_info)
                self.dragon_card_data_controller = DragonCardDataController(game.dragon_cards)
                # print(self.player_data_controller.get_players() , self.dragon_card_data_controller.get_dragon_cards())
                self.location_data_controller = LocationDataController(game.tiles, game.caves , self.player_data_controller.get_players())

    def load_from_default_config(self):
        pass

    def get_saved_games(self) -> List[GameProgressData]:
        return self.game_progress_list
