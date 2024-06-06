from typing import List
from Player import Player
from Tile import Tile
from PlayerMoveController import PlayerMoveController
from PlayerDataController import IPlayerDataController
from LocationDataController import ILocationDataController
from LocationManager import LocationManager


class SpecialEffectController:
    def __init__(self, player_data_controller: IPlayerDataController, location_manager: LocationManager):

        self.player_data_controller = player_data_controller
        self.location_manager = location_manager

    def apply_special_effect(self, current_player: Player):
        # Find the closest player to the current player
        closest_player = self.find_closest_player(current_player)

        if closest_player is not None:
            # Swap the positions of the current player and the closest player
            current_player_square = self.location_manager.get_player_location(current_player)
            closest_player_square = self.location_manager.get_player_location(closest_player)

            self.location_manager.remove_player_location(current_player_square)
            self.location_manager.remove_player_location(closest_player_square)

            self.location_manager.set_player_location(current_player, closest_player_square)
            self.location_manager.set_player_location(closest_player, current_player_square)

    def find_closest_player(self, current_player: Player) -> Player or None:
        players = self.player_data_controller.get_players()
        current_player_square = self.location_manager.get_player_location(current_player)

        closest_player = None
        min_distance = float('inf')

        for player in players:
            player_square = self.location_manager.get_player_location(player)
            if player != current_player and not player_square.is_cave():
                distance = len(self.location_manager.get_tiles_between(current_player_square, player_square))

                if distance < min_distance:
                    min_distance = distance
                    closest_player = player

        return closest_player

    # def calculate_distance(self, tile1: Tile, tile2: Tile) -> int:
    #     # squares = self.location_data_controller.get_squares()
    #     # index1 = squares.index(tile1)
    #     # index2 = squares.index(tile2)
    #     #
    #     # distance = min(abs(index1 - index2), len(squares) - abs(index1 - index2))
    #     # return distance
    #     distance = len(self.location_manager.get_tiles_between(tile1, tile2))
    #     return distance