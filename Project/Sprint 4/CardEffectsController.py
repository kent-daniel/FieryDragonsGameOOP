from Square import Square
from DragonCard import AnimalDragonCard
from DragonCard import PirateDragonCard
from DragonCard import SpecialDragonCard
from PlayerMoveController import PlayerMoveController
from SpecialEffectController import SpecialEffectController
from Movement import Movement
from Player import Player


class CardEffectsController:
    def __init__(self):
        self.visitors = {
            AnimalDragonCard: AnimalDragonCardEffectVisitor,
            PirateDragonCard: PirateDragonCardEffectVisitor
        }

    def get_visitor(self, card):
        visitor_class = self.visitors.get(type(card))
        if visitor_class:
            return visitor_class(card.value)
        else:
            raise ValueError(f"Unsupported card type: {type(card)}")