from MovementEventManager import IMovementEventListener
from PlayerDataController import IPlayerDataController
from LocationManager import LocationManager
from PlayerTurnController import IPlayerTurnController
from Movement import Movement
from NotificationManager import NotificationManager


class PlayerLivesManager(IMovementEventListener):

    """
    Manager to handle player lives based on movement events.

    Attributes:
        player_data_controller (IPlayerDataController): Controller to manage player data.
        player_turn_controller (IPlayerTurnController): Controller to manage player turns.
        location_manager (LocationManager): Manager to handle player locations.
        notification_manager (NotificationManager): Manager to handle notifications.
    """

    def __init__(self,
                 player_data_controller: IPlayerDataController,
                 player_turn_controller: IPlayerTurnController,
                 location_manager: LocationManager,
                 notification_manager: NotificationManager = NotificationManager()):
        self.player_data_controller = player_data_controller
        self.player_turn_controller = player_turn_controller
        self.location_manager = location_manager
        self.notification_manager = notification_manager

    def on_movement_event(self, movement: Movement) -> None:
        """
        Handles a movement event to update player lives.
        Reduces lives if the player fails to move and eliminates the player if lives reach zero.

        Args:
            movement (Movement): The movement event.
        """
        current_player = self.player_turn_controller.get_current_player()
        if movement.value == 0:  # reduce lives if player fails to move
            current_player.lives -= 1
            self.player_data_controller.update_player(current_player)
            self.notification_manager.add_notification(
                f" player {current_player.id} has {current_player.lives} lives remaining", "warning")

        if current_player.lives <= 1:  # remove player if player runs out of lives
            self.eliminate_player(current_player)

        if not self.player_data_controller.get_players():
            return

    def eliminate_player(self, current_player):
        """
        Eliminates the player by removing their data and location.
        Sends a notification about the elimination.

        Args:
            current_player (Player): The player to be eliminated.
        """
        self.notification_manager.add_notification(f"Player {current_player.id} has been eliminated.", "warning")
        current_player_location = self.location_manager.get_player_location(current_player)
        self.location_manager.remove_player_location(current_player_location)
        self.player_data_controller.delete_player(current_player.id)
