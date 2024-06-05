from abc import ABC, abstractmethod
from Player import Player
from Movement import Movement
from MovementEventManager import IMovementEventManager
from PlayerDataController import IPlayerDataController
from LocationDataController import ILocationDataController
from NotificationManager import NotificationManager
from Tile import Tile


class IPlayerMoveController(ABC):

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

    def move_forward(self, player: Player, origin_location: Tile, steps: int) -> Movement:
        destination = origin_location
        for step in range(steps):
            destination = destination.next

        if player.steps_to_win - steps < 0:
            self._notification_manager.add_notification(f"Player {player.id} cannot pass cave")
            return Movement(0, origin_location)
        if player.steps_to_win == steps:  # move player to cave
            return Movement(steps, destination if destination.is_cave() else destination.cave)  # return the movement to the cave
        if self._check_destination_is_occupied(destination):  # check if destination is occupied
            return Movement(0, origin_location)
        return Movement(steps, destination)

    def move_backward(self, player: Player, origin_location: Tile, steps: int) -> Movement:
        destination = origin_location
        for step in range(steps):
            if origin_location.is_cave() or destination.cave and destination.cave.get_owner().id == player.id:  # if player is passing their cave
                self._notification_manager.add_notification(f"player {player.id} cannot go behind cave")
                return Movement(0, origin_location)
            destination = destination.prev
        if self._check_destination_is_occupied(destination):  # check if destination is occupied
            return Movement(0, origin_location)
        return Movement(-steps, destination)

    def _check_destination_is_occupied(self, destination: Tile) -> bool:
        if destination.get_occupant() is None:
            return False
        self._notification_manager.add_notification(f"destination is occupied")
        return True
