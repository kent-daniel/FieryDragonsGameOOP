from ICardEffectsController import ICardEffectsController
from SpecialEffectController import SpecialEffectController
from PlayerMoveController import PlayerMoveController
from Movement import Movement
from Player import Player


class CardEffectsController(ICardEffectsController):
    def __init__(self, player_move_controller: PlayerMoveController,
                 special_effect_controller: SpecialEffectController):
        self.player_move_controller = player_move_controller
        self.special_effect_controller = special_effect_controller

    # def get_visitor(self, card):
    #     visitor_class = self.visitors.get(type(card))
    #     if visitor_class:
    #         return visitor_class(card.value)
    #     else:
    #         raise ValueError(f"Unsupported card type: {type(card)}")

    def animal_effect(self, animal_card, player: Player):
        square = self.player_move_controller.get_player_location(player)
        if square.character != animal_card.character:
            self.player_move_controller.process_movement(player, Movement(0, square))
            return
        destination = square
        for i in range(animal_card.value):
            destination = destination.next

        self.player_move_controller.process_movement(player, Movement(animal_card.value, destination))

    def pirate_effect(self, pirate_card, player: Player):
        square = self.player_move_controller.get_player_location(player)
        destination = square
        for i in range(pirate_card.value):
            destination = destination.prev
        self.player_move_controller.process_movement(player, Movement(-pirate_card.value, destination))

    def special_effect(self, special_card, player: Player):
        self.special_effect_controller.apply_special_effect(player)
