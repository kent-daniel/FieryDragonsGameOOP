from abc import ABC, abstractmethod
from typing import List

from Player import Player
from Movement import Movement
from Square import Square
from MovementEventManager import IMovementEventManager
from GameDataController import IPlayerDataController, ILocationDataController
from NotificationManager import NotificationManager
from DragonCard import DragonCard
from Tile import Tile


class IPlayerMoveController(ABC):
    @abstractmethod
    def process_movement(self, player: Player, card: DragonCard):
        pass

    @abstractmethod
    def update_player_location(self, player: Player, square: Square) -> None:
        pass

    @abstractmethod
    def get_player_location(self, player) -> Square:
        pass


class PlayerMoveController(IPlayerMoveController):
    """
        PlayerMoveController

        This class implements the IPlayerMoveController interface and manages player movements,
        updates player locations, and handles notifications and event publishing.

        Attributes:
            movement_publisher (IMovementEventManager): used to publish movement events.
            data_controller (IPlayerDataController): Manages player data.
            notification_manager (NotificationManager): used to add notifications.

        Methods:
            process_movement(player: Player, card: DragonCard):
                Process the player's movement based on the DragonCard drawn.
            update_player_location(player: Player, square: Square) -> None:
                Updates the player's location to the specified square.
            get_player_location(player: Player) -> Square:
                Returns the current location of the player.
        """

    def __init__(self, movement_publisher: IMovementEventManager, player_data_controller: IPlayerDataController,
                 location_data_controller: ILocationDataController,
                 notification_manager=NotificationManager()):
        self._movement_publisher = movement_publisher
        self._player_data_controller = player_data_controller
        self._location_data_controller = location_data_controller
        self._notification_manager = notification_manager

    def process_movement(self, player: Player, card: DragonCard):
        player_location = self.get_player_location(
            player)
        print(player_location)
        final_movement = self._validate_and_return_movement(card.action(player_location), player, player_location)
        player.steps_to_win -= final_movement.value

    def _validate_and_return_movement(self, movement: Movement, player: Player, player_location: Tile) -> Movement:
        final_movement = movement
        #print(self.get_tiles_between(player_location, movement.destination))
        # player can only move to their own cave
        if movement.destination.is_cave() and movement.destination.get_owner() != player:
            final_movement = Movement(movement.value, movement.destination.next)
        if final_movement.value == 0:
            self._notification_manager.add_notification(f"player {player.id} didn't get a matching card")
        # elif self._check_destination_is_occupied(final_movement) or self._player_passing_cave(player, player_location,
        #                                                                                       final_movement):
        #     final_movement = Movement(0, player_location)
        elif final_movement.value != 0:

            self.update_player_location(player, final_movement.destination)
            self._notification_manager.add_notification(
                f"player {player.id} is moving to Tile {final_movement.destination.id}")
        else:
            self._notification_manager.add_notification(f"player {player.id} didn't move")

        self._movement_publisher.publish_event(final_movement)
        return final_movement

    def _check_destination_is_occupied(self, movement: Movement) -> bool:
        if movement.destination.get_occupant() is None:
            return False
        self._notification_manager.add_notification(f"destination is occupied")
        return True

    def _player_passing_cave(self, player: Player, starting_tile: Tile, movement: Movement) -> bool:
        # player cannot go backwards from initial game starting position
        if movement.value < 0 and starting_tile.is_cave() and starting_tile.get_owner().id == player.id:
            self._notification_manager.add_notification(f"player {player.id} cannot go behind cave")
            return True
        square: Square = starting_tile
        steps = abs(movement.value)
        for step in range(steps):
            if movement.value < 0:
                square = square.prev
            else:
                square = square.next
            if square.cave and square.cave.get_owner().id == player.id and step + 1 < steps:  # check if player got into a cave before finishing movement
                self._notification_manager.add_notification(f"player {player.id} cannot pass cave")
                return True
        return False

    def update_player_location(self, player: Player, tile: Tile) -> None:
        current_location = self.get_player_location(player)
        squares = self._location_data_controller.get_squares()
        for i in range(len(squares)):
            if current_location.is_cave() and squares[i].cave and squares[i].cave.get_occupant() and squares[i].cave.get_occupant().id == player.id:
                squares[i].cave.remove_occupant()
            if squares[i] == current_location:
                squares[i].remove_occupant()
            if squares[i] == tile:
                squares[i].set_occupant(player)
        self._location_data_controller.set_squares(squares)

    def get_tiles_between(self, tile_1: Tile, tile_2: Tile) -> List[Tile]:
        """Get all tiles between two tiles, the output will be the shortest tiles path to between tile_1 and tile_2"""
        if tile_1 == tile_2:
            return [tile_1]

        forward_tiles_1 = []
        forward_tiles_2 = []

        current_tile_1 = tile_1
        current_tile_2 = tile_2

        # Simultaneous traversal from both tiles
        while True:
            if current_tile_1 is not None:
                forward_tiles_1.append(current_tile_1)
                if current_tile_1 == tile_2:
                    return forward_tiles_1
                current_tile_1 = current_tile_1.next

            if current_tile_2 is not None:
                forward_tiles_2.append(current_tile_2)
                if current_tile_2 == tile_1:
                    return forward_tiles_2[::-1]
                current_tile_2 = current_tile_2.next

            # If we reach the end in either direction without finding the target tile
            if current_tile_1 is None and current_tile_2 is None:
                break

    def get_player_location(self, player) -> Tile:
        for square in self._location_data_controller.get_squares():
            if square.get_occupant() and square.get_occupant().id == player.id:
                return square
            if square.cave and square.cave.get_occupant() and square.cave.get_occupant().id == player.id:
                return square.cave
