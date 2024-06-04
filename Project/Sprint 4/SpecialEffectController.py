from typing import List
from Player import Player
from Square import Square
from PlayerMoveController import PlayerMoveController
from GameDataController import IPlayerDataController

class SpecialEffectController:
    def __init__(self, player_move_controller: PlayerMoveController, player_data_controller: IPlayerDataController):
        self.player_move_controller = player_move_controller
        self.player_data_controller = player_data_controller

    def apply_special_effect(self, current_player: Player):
        # Find the closest player to the current player
        closest_player = self.find_closest_player(current_player)

        if closest_player is not None:
            # Swap the positions of the current player and the closest player
            current_player_square = self.player_move_controller.get_player_location(current_player)
            closest_player_square = self.player_move_controller.get_player_location(closest_player)

            self.player_move_controller.update_player_location(current_player, closest_player_square)
            self.player_move_controller.update_player_location(closest_player, current_player_square)

    def find_closest_player(self, current_player: Player) -> Player or None:
        players = self.player_data_controller.get_players()
        current_player_square = self.player_move_controller.get_player_location(current_player)

        closest_player = None
        min_distance = float('inf')

        for player in players:
            if player != current_player:
                player_square = self.player_move_controller.get_player_location(player)
                distance = self.calculate_distance(current_player_square, player_square)

                if distance < min_distance:
                    min_distance = distance
                    closest_player = player

        return closest_player

    def calculate_distance(self, square1: Square, square2: Square) -> int:
        squares = self.player_data_controller.get_squares()
        index1 = squares.index(square1)
        index2 = squares.index(square2)

        distance = min(abs(index1 - index2), len(squares) - abs(index1 - index2))
        return distance