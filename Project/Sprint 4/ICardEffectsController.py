from abc import ABC, abstractmethod
from Player import Player


class ICardEffectsController(ABC):
    @abstractmethod
    def animal_effect(self, animal_card, player: Player):
        pass

    @abstractmethod
    def pirate_effect(self, pirate_card, player: Player):
        pass

    @abstractmethod
    def special_effect(self, special_card, player: Player):
        pass
