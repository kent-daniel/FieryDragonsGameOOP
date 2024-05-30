from DragonCard import AnimalDragonCard, PirateDragonCard
from CardEffectVisitor import AnimalDragonCardEffectVisitor, PirateDragonCardEffectVisitor

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