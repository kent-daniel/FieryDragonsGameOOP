from abc import ABC, abstractmethod
from Player import Player
from Movement import Movement
from Square import Square
from MovementEventManager import IMovementEventManager
from PlayerDataController import IPlayerDataController
from LocationDataController import ILocationDataController
from NotificationManager import NotificationManager
from Tile import Tile


class IPlayerMoveController(ABC):
    @abstractmethod
    def process_movement(self, player: Player):
        pass

    @abstractmethod
    def move_forward(self, player: Player, origin_location: Tile, steps: int) -> Movement:
        pass

    @abstractmethod
    def move_backward(self, player: Player, origin_location: Tile, steps: int) -> Movement:
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

    def __init__(self, player_data_controller: IPlayerDataController,
                 notification_manager=NotificationManager()):

        self._player_data_controller = player_data_controller
        self._notification_manager = notification_manager

    def process_movement(self, player: Player, movement: Movement, player_location: Tile) -> Movement:
        final_movement = self._validate_and_return_movement(movement, player, player_location)

        return final_movement

    def move_forward(self, player: Player, origin_location: Tile, steps: int) -> Movement:
        destination = origin_location
        for step in range(steps):
            destination = destination.next
            # if destination.cave and destination.cave.get_occupant() and destination.cave.get_occupant().id == player.id:
            #     if step < steps - 1:  # if player is passing cave but not at the final step
            #         self._notification_manager.add_notification(f"Player {player.id} cannot pass cave")
            #         return Movement(0, origin_location)
            #     else:  # move player to enter cave
            #         return Movement(step + 1, destination if destination.is_cave() else destination.cave)  # return the movement to the cave
        if destination.get_occupant():  # check if destination is occupied
            self._notification_manager.add_notification(f"destination is occupied")
        return Movement(steps, destination)

    def move_backward(self, player: Player, origin_location: Tile, steps: int) -> Movement:
        destination = origin_location
        for step in range(steps):
            if destination.is_cave() or destination.cave and destination.cave.get_occupant().id == player.id and step < steps - 1: # if player is passing cave but not at the final step
                self._notification_manager.add_notification(f"player {player.id} cannot go behind cave")
                return Movement(0, origin_location)
            destination = destination.prev
        if destination.get_occupant():
            self._notification_manager.add_notification(f"destination is occupied")
        return Movement(-steps, destination)

    def _validate_and_return_movement(self, movement: Movement, player: Player, player_location: Tile) -> Movement:
        final_movement = movement
        #print(self.get_tiles_between(player_location, movement.destination))
        # player can only move to their own cave
        if movement.destination.is_cave() and movement.destination.get_owner().id != player.id:
            final_movement = Movement(movement.value, movement.destination.next)
        if final_movement.value == 0:
            self._notification_manager.add_notification(f"player {player.id} didn't get a matching card")
        # elif self._check_destination_is_occupied(final_movement) or self._player_passing_cave(player, player_location,
        #                                                                                       final_movement):
        #     final_movement = Movement(0, player_location)
        elif final_movement.value != 0:
            self._notification_manager.add_notification(
                f"player {player.id} is moving to Tile {final_movement.destination.id}")
        else:
            self._notification_manager.add_notification(f"player {player.id} didn't move")
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
