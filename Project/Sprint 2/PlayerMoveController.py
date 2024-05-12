from abc import ABC, abstractmethod
from Player import Player
from Movement import Movement
from Square import Square
from MovementEventManager import IMovementEventManager
from GameDataController import IPlayerDataController


class IPlayerMoveController(ABC):
    @abstractmethod
    def process_movement(self, player_location, player: Player, movement: Movement) -> Movement:
        pass

    @abstractmethod
    def update_player_location(self, player: Player, square: Square) -> None:
        pass

    @abstractmethod
    def get_player_location(self, player) -> Square:
        pass


class PlayerMoveController(IPlayerMoveController):
    def __init__(self, movement_publisher: IMovementEventManager, data_controller: IPlayerDataController):
        self._movement_publisher = movement_publisher
        self._data_controller = data_controller

    def process_movement(self, player_location: Square, player: Player, movement: Movement) -> Movement:
        final_movement = movement
        if movement.destination.get_occupant() is not None or self._player_passing_cave(player, player_location,                                                                            movement):
            final_movement = Movement(0, player_location)
        else:
            self.update_player_location(player, movement.destination)
        self._movement_publisher.publish_event(final_movement)
        return movement

    def _player_passing_cave(self, player: Player, starting_square: Square, movement: Movement) -> bool:
        # player cannot go backwards from initial game starting position
        if movement.value < 0 and starting_square.cave and starting_square.cave.get_owner() == player:
            return True
        square = starting_square
        for i in range(abs(movement.value)):
            if movement.value < 0:
                square = square.prev
            else:
                square = square.next
            if square.cave and square.cave.get_owner() == player and movement.value < 0:
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
