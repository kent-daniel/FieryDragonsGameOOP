from abc import ABC, abstractmethod
from typing import List

from Player import Player
from Movement import Movement
from Square import Square
from MovementEventManager import IMovementEventManager
from GameDataController import GameDataController
from VolcanoCard import VolcanoCard


class IPlayerMoveController(ABC):
    @abstractmethod
    def process_movement(self, player: Player, movement: Movement) -> Movement:
        pass

    @abstractmethod
    def update_player_location(self, player: Player, square: Square) -> None:
        pass

    @abstractmethod
    def get_player_location(self, player) -> Square:
        pass


class PlayerMoveController(IPlayerMoveController):
    def __init__(self, movement_publisher: IMovementEventManager, data_controller: GameDataController):
        self._movement_publisher = movement_publisher
        self._data_controller = data_controller

    def process_movement(self, player: Player, movement: Movement) -> Movement:
        current_player_loc = self.get_player_location(player)
        if movement.destination.get_occupant() is not None: return Movement(0, current_player_loc)
        if self._player_passing_cave(player, current_player_loc, movement): return Movement(0, current_player_loc)
        self._movement_publisher.publish_event(movement)

        return movement

    def _player_passing_cave(self, player: Player, starting_square: Square, movement: Movement) -> bool:
        square = starting_square
        for _ in range(abs(movement.value)):
            if movement.value < 0:
                square = square.prev
            else:
                square = square.next
            if square.cave.get_owner() == player:
                return True
        return False

    def update_player_location(self, player: Player, square: Square) -> None:
        volcano_cards: List[VolcanoCard] = self._data_controller.get_volcano_cards()
        current_location = self.get_player_location(player)
        for card in volcano_cards:
            card.squares = [sq.remove_player() if sq == current_location else sq for sq in card.squares]
        for card in volcano_cards:
            card.squares = [sq.set_occupant(player) if sq == square else sq for sq in card.squares]
        self._data_controller.set_volcano_cards(volcano_cards)

    def get_player_location(self, player) -> Square:
        volcano_cards = self._data_controller.get_volcano_cards()
        for volcano in volcano_cards:
            for square in volcano.squares:
                if square.get_occupant() == player:
                    return square
