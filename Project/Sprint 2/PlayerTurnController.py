from abc import abstractmethod
from Player import Player
from MovementEventManager import IMovementEventListener
from Movement import Movement
from GameDataController import IPlayerDataController


class IPlayerTurnController(IMovementEventListener):

    @abstractmethod
    def get_current_player(self) -> Player:
        pass

    @abstractmethod
    def switch_player(self) -> None:
        pass


class PlayerTurnController(IPlayerTurnController):

    def __init__(self, data_controller: IPlayerDataController):
        self._data_controller = data_controller
        self._players = self._data_controller.get_players()

    def get_current_player(self) -> Player:
        return self._players[0]

    def on_movement_event(self, movement: Movement) -> None:
        if movement.value == 0:
            self.switch_player()

    def switch_player(self):
        pass
