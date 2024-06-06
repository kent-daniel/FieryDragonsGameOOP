from typing import List
from Player import Player
from Tile import Tile
from PlayerMoveController import PlayerMoveController
from PlayerDataController import IPlayerDataController
from LocationDataController import ILocationDataController
from LocationManager import LocationManager
from NotificationManager import NotificationManager


class SpecialEffectController:
    def __init__(self, player_data_controller: IPlayerDataController, location_manager: LocationManager, notification_manager=NotificationManager()):

        self.player_data_controller = player_data_controller
        self.location_manager = location_manager
        self.notification_manager = notification_manager

    def apply_special_effect(self, current_player: Player):
        # Find the closest player to the current player
        closest_player = self.find_closest_player(current_player)

        if closest_player is not None:
            # Swap the positions of the current player and the closest player
            current_player_square = self.location_manager.get_player_location(current_player)
            closest_player_square = self.location_manager.get_player_location(closest_player)

            distance_forward = len(self.location_manager.get_closest_forward(current_player_square, closest_player_square))
            distance_backward = len(self.location_manager.get_closest_backward(current_player_square, closest_player_square))
            if distance_backward < distance_forward:
                # if current player stepstowin > 26 then - 26 and opposite for closest
                current_player.steps_to_win += distance_backward
                closest_player.steps_to_win -= distance_backward
                if current_player.steps_to_win > 26:
                    current_player.steps_to_win -= 26
                if closest_player.steps_to_win < 0:
                    closest_player.steps_to_win += 26
            else:
                # if current player stepstowin < 0 then + 26 and opposite for closest
                current_player.steps_to_win -= distance_forward
                closest_player.steps_to_win += distance_forward
                if current_player.steps_to_win < 0:
                    current_player.steps_to_win += 26
                if closest_player.steps_to_win > 26:
                    closest_player.steps_to_win -= 26
            # update player data

            self.player_data_controller.update_player(current_player)
            self.player_data_controller.update_player(closest_player)

            # Remove the current player's location from the location manager
            # Remove the closest player's location from the location manager
            # Set the current player's location to the closest player's location
            # Set the closest player's location to the current player's location
            # Add a notification to the notification manager saying that the players were swapped

            self.location_manager.remove_player_location(current_player_square)
            self.location_manager.remove_player_location(closest_player_square)

            self.location_manager.set_player_location(current_player, closest_player_square)
            self.location_manager.set_player_location(closest_player, current_player_square)

            self.notification_manager.add_notification(f"player {current_player.id} and player {closest_player.id} swapped")
        else:
            self.notification_manager.add_notification(f"Players in cave cannot be swapped")

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
