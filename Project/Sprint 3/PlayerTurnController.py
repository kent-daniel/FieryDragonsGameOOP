from abc import abstractmethod
from Player import Player
from MovementEventManager import IMovementEventListener
from Movement import Movement
from GameDataController import IPlayerDataController
from NotificationManager import NotificationManager

# Garv Vohra
class IPlayerTurnController(IMovementEventListener):

    @abstractmethod
    def get_current_player(self) -> Player:
        pass

    @abstractmethod
    def switch_player(self) -> None:
        pass

#Garv Vohra
class PlayerTurnController(IPlayerTurnController):

    def __init__(self, data_controller: IPlayerDataController, notification_manager=NotificationManager()):
        self._data_controller = data_controller
        self._players = self._data_controller.get_players()
        self._notification_manager = notification_manager
        self.current_player = self._players[0]

    def get_current_player(self) -> Player:
        return self.current_player

    def on_movement_event(self, movement: Movement) -> None:
        if movement.value == 0:
            self.switch_player()

    def switch_player(self):
        player_index = (self.current_player.id + 1) % self._players.__len__()
        self.current_player = self._players[player_index-1]
        self._notification_manager.add_notification(f"switching to player {self.get_current_player().id}'s turn")

