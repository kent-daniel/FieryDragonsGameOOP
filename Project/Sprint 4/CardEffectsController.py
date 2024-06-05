from ICardEffectsController import ICardEffectsController
from SpecialEffectController import SpecialEffectController
from PlayerMoveController import PlayerMoveController
from Movement import Movement
from Player import Player
from LocationManager import LocationManager


class CardEffectsController(ICardEffectsController):
    def __init__(self, player_move_controller: PlayerMoveController,
                 special_effect_controller: SpecialEffectController, location_manager: LocationManager):
        self.player_move_controller = player_move_controller
        self.special_effect_controller = special_effect_controller
        self.location_manager = location_manager

    # def get_visitor(self, card):
    #     visitor_class = self.visitors.get(type(card))
    #     if visitor_class:
    #         return visitor_class(card.value)
    #     else:
    #         raise ValueError(f"Unsupported card type: {type(card)}")

    def animal_effect(self, animal_card, player: Player):
        square = self.location_manager.get_player_location(player)
        if square.character != animal_card.character:
            final_movement = self.player_move_controller.process_movement(player, Movement(0, square),square)
            self.location_manager.update_player_location(player, final_movement.destination)
        destination = square
        for i in range(animal_card.value):
            destination = destination.next

        final_movement = self.player_move_controller.process_movement(player, Movement(animal_card.value, destination),square)
        self.location_manager.update_player_location(player, final_movement.destination)


    def pirate_effect(self, pirate_card, player: Player):
        square = self.location_manager.get_player_location(player)
        destination = square
        for i in range(pirate_card.value):
            destination = destination.prev
        final_movement = self.player_move_controller.process_movement(player, Movement(-pirate_card.value, destination),square)
        self.location_manager.update_player_location(player, final_movement.destination)


    def special_effect(self, special_card, player: Player):
        self.special_effect_controller.apply_special_effect(player)
