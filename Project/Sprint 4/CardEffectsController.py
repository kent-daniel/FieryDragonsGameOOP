from ICardEffectsController import ICardEffectsController
from SpecialEffectController import SpecialEffectController
from PlayerMoveController import IPlayerMoveController
from Movement import Movement
from Player import Player
from LocationManager import LocationManager
from MovementEventManager import IMovementEventManager
from NotificationManager import NotificationManager


class CardEffectsController(ICardEffectsController):
    def __init__(self, player_move_controller: IPlayerMoveController,
                 special_effect_controller: SpecialEffectController,
                 location_manager: LocationManager,
                 movement_publisher: IMovementEventManager,
                 notification_manager: NotificationManager = NotificationManager()):
        self.player_move_controller = player_move_controller
        self.special_effect_controller = special_effect_controller
        self.location_manager = location_manager
        self.movement_publisher = movement_publisher
        self._notification_manager = notification_manager

    def animal_effect(self, animal_card, player: Player):
        current_square = self.location_manager.get_player_location(player)
        final_movement: Movement = Movement(animal_card.value, current_square)
        if current_square.character != animal_card.character:
            final_movement = Movement(0, current_square)
            self._notification_manager.add_notification(f"player {player.id} didn't get a matching card")
        else:
            final_movement = self.player_move_controller.move_forward(player, current_square, animal_card.value)

        if final_movement.value != 0:
            self.location_manager.remove_player_location(current_square)
            self.location_manager.set_player_location(player, final_movement.destination)
            self._notification_manager.add_notification(f"player {player.id} is moving forward to tile {final_movement.destination.id}")
            player.steps_to_win -= final_movement.value
        self.movement_publisher.publish_event(final_movement)

    def pirate_effect(self, pirate_card, player: Player):
        current_square = self.location_manager.get_player_location(player)

        final_movement = self.player_move_controller.move_backward(player, current_square,pirate_card.value)

        if final_movement.value != 0:
            self.location_manager.remove_player_location(current_square)
            self.location_manager.set_player_location(player, final_movement.destination)
            self._notification_manager.add_notification(f"player {player.id} is moving back to tile {final_movement.destination.id}")
            player.steps_to_win += final_movement.value
        self.movement_publisher.publish_event(final_movement)


    def special_effect(self, special_card, player: Player):
            self.special_effect_controller.apply_special_effect(player)
