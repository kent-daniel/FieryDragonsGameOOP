from abc import ABC, abstractmethod
from Player import Player
from Movement import Movement
from Square import Square
from MovementEventManager import IMovementEventManager
from GameDataController import IPlayerDataController
from NotificationManager import NotificationManager
from DragonCard import DragonCard
import CardEffectsController


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
    def __init__(self, movement_publisher: IMovementEventManager, data_controller: IPlayerDataController,
                 card_effects_controller: CardEffectsController, notification_manager=NotificationManager()):
        self._movement_publisher = movement_publisher
        self._data_controller = data_controller
        self._notification_manager = notification_manager
        self.card_effects_controller = card_effects_controller

    def process_movement(self, player: Player, movement: Movement):
        player_location = self.get_player_location(player)
        final_movement = self._validate_and_return_movement(movement, player, player_location)
        player.steps_to_win -= final_movement.value

    def _validate_and_return_movement(self, movement: Movement, player: Player, player_location: Square) -> Movement:
        final_movement = movement
        if final_movement.value == 0:
            self._notification_manager.add_notification(f"player {player.id} didn't get a matching card")
        elif self._check_destination_is_occupied(final_movement) or self._player_passing_cave(player, player_location,
                                                                                        final_movement):
            final_movement = Movement(0, player_location)
        elif final_movement.value != 0:
            self.update_player_location(player, final_movement.destination)
            self._notification_manager.add_notification(
                f"player {player.id} is moving to Square {final_movement.destination.id}")
        else:
            self._notification_manager.add_notification(f"player {player.id} didn't move")

        self._movement_publisher.publish_event(final_movement)
        return final_movement

    def _check_destination_is_occupied(self, movement: Movement) -> bool:
        if movement.destination.get_occupant() is None:
            return False
        self._notification_manager.add_notification(f"destination is occupied")
        return True

    def _player_passing_cave(self, player: Player, starting_square: Square, movement: Movement) -> bool:
        # player cannot go backwards from initial game starting position
        if movement.value < 0 and starting_square.cave and starting_square.cave.get_owner().id == player.id:
            self._notification_manager.add_notification(f"player {player.id} cannot go behind cave")
            return True
        square = starting_square
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

    def update_player_location(self, player: Player, square: Square) -> None:
        current_location = self.get_player_location(player)
        squares = self._data_controller.get_squares()
        for i in range(len(squares)):
            if squares[i] == current_location:
                squares[i].remove_player()
            if squares[i] == square:
                squares[i].set_occupant(player)
        self._data_controller.set_squares(squares)

    def get_player_location(self, player) -> Square:
        for square in self._data_controller.get_squares():
            if square.get_occupant() and square.get_occupant().id == player.id:
                return square
