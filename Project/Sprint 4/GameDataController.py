import json
import os
import sys
from PlayerDataController import IPlayerDataController, PlayerDataController
from DragonCardDataController import IDragonCardDataController, DragonCardDataController


class GameDataController:
    def __init__(self, config_path: str = 'config.json'):
        self.config = self._parse_config(config_path)

    def _parse_config(self, config_path: str) -> dict:
        filepath = self.get_packaged_files_path()
        filename = os.path.join(filepath, config_path)
        # print(f"Current working directory: {os.getcwd()}")  # Debugging line
        # print(f"Attempting to load config file from: {filename}")  # Debugging line
        with open(filename, 'r') as config_file:
            config = json.load(config_file)

        return config

    def create_player_data_controller(self) -> IPlayerDataController:
        return PlayerDataController(self.config['square_animals'], self.config['player_count'])

    # def create_location_data_controller(self) ->ILocationDataController:
    #     return LocationDataController()

    def create_dragon_card_data_controller(self) -> IDragonCardDataController:
        return DragonCardDataController(self.config['dragon_cards'])

    def get_packaged_files_path(self):
        """Location of relative paths """
        if getattr(sys, 'frozen', False):
            path = sys._MEIPASS
        else:
            path = '.'

        return path
