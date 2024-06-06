from abc import abstractmethod
from Player import Player
from MovementEventManager import IMovementEventListener
from Movement import Movement
from GameDataController import IPlayerDataController
from NotificationManager import NotificationManager
from queue import Queue
from TimerController import TimerController

class IPlayerTurnController(IMovementEventListener):
    """
    Author: Garv Vohra
    Interface for controlling player turns in a game. Inherits from IMovementEventListener to handle movement events.
    """

    @abstractmethod
    def get_current_player(self) -> Player:
        """
        Abstract method to get the current player.

        Returns:
            Player: The current player.
        """
        pass

    @abstractmethod
    def switch_player(self) -> None:
        """
        Abstract method to switch to the next player.
        """
        pass
    @abstractmethod
    def check_time(self):
        pass


#Garv Vohra
class PlayerTurnController(IPlayerTurnController):
    """
    Author: Garv Vohra
    Concrete implementation of IPlayerTurnController to manage player turns in a game.

    Attributes:
        _data_controller (IPlayerDataController): Controller to manage player data.
        _players (list[Player]): List of players in the game.
        _notification_manager (NotificationManager): Manager to handle notifications.
        current_player (Player): The current player.
    """

    TURN_TIME_LIMIT = 15  # Time limit for each turn in seconds

    def __init__(self, data_controller: IPlayerDataController, timer: TimerController, notification_manager=NotificationManager()):
        self._data_controller = data_controller
        self._players = self._data_controller.get_players()
        self._notification_manager = notification_manager
        self.timer = timer
        self.current_player = self._data_controller.get_players()[0]


    def get_current_player(self) -> Player:
        """
        Gets the current player.

        Returns:
            Player: The current player.
        """
        return self.current_player

    def on_movement_event(self, movement: Movement) -> None:
        """
        Handles a movement event. If the movement value is 0, it switches to the next player.

        Args:
            movement (Movement): The movement event.
        """
        if movement.value == 0:
            self.switch_player()

    def switch_player(self):
        """
        Switches to the next player and sends a notification about the switch.
        """

        self._data_controller.get_players().rotate(-1)
        self.current_player = self._data_controller.get_players()[0]
        self._notification_manager.add_notification(f"switching to player {self.get_current_player().id}'s turn")
        self.timer.update_time()


    def check_time(self):
        time = float(self.timer.get_time())
        if time <= 0:
            self.switch_player()

