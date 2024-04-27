import random
from abc import ABC, abstractmethod
from typing import List
from DragonCard import DragonCard, PirateDragonCard, AnimalDragonCard
from GameConstants import CharacterImage


class IDragonCardDataController(ABC):
    @abstractmethod
    def get_dragon_cards(self) -> List[DragonCard]:
        pass


class DragonCardDataController(IDragonCardDataController):
    def __init__(self, dragon_card_config_data: str):
        self._config_data = dragon_card_config_data
        self._dragon_cards: List[DragonCard] = []
        self.load_data()

    def get_dragon_cards(self) -> List[DragonCard]:
        return self._dragon_cards

    def load_data(self) -> None:
        dragons = self._config_data.split(",")
        dragon_cards: List[DragonCard] = []
        for dragon in dragons:
            value, character = dragon.split("x")
            if character == CharacterImage.PIRATE.name:
                dragon_cards.append(PirateDragonCard(CharacterImage[character], int(value)))
            else:
                dragon_cards.append(AnimalDragonCard(CharacterImage[character], int(value)))

        random.shuffle(dragon_cards)
        self._dragon_cards = dragon_cards
