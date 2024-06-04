import random
from abc import ABC, abstractmethod
from typing import List
from DragonCard import DragonCard, PirateDragonCard, AnimalDragonCard
from GameConstants import CharacterImage


class IDragonCardDataController(ABC):
    """
    IDragonCardDataController

    Authored by: Vansh Batas

    This abstract base class defines the interface for a data controller responsible
    for managing a list of DragonCard objects.

    Methods:
       @abstractmethod get_dragon_cards() -> List[DragonCard]:
           Returns the list of DragonCard objects.
       @abstractmethod set_dragon_cards(dragon_cards: List[DragonCard]) -> None:
           Sets the list of DragonCard objects.
    """

    @abstractmethod
    def get_dragon_cards(self) -> List[DragonCard]:
        """
        The get_dragon_cards function returns a list of DragonCard objects.

        :param self: Access the class attributes and methods
        :return: A list of dragoncard objects
        """
        pass

    @abstractmethod
    def set_dragon_cards(self, dragon_cards: List[DragonCard]) -> None:
        """
        The set_dragon_cards function is used to set the dragon cards for a player.

        :param self: Represent the instance of the class
        :param dragon_cards: List[DragonCard]: Specify the type of data that is being passed into the function
        :return: None
        """
        pass

    @abstractmethod
    def to_json_format(self) -> List[dict]:
        pass

class DragonCardDataController(IDragonCardDataController):
    """
    DragonCardDataController

    Authored by: Vansh Batas

    This class implements the IDragonCardDataController interface and provides functionality
    for loading and managing a list of DragonCard objects from a configuration string.

    Methods:
       __init__(dragon_card_config_data: str) -> None:
           Initializes the DragonCardDataController with a configuration string.
       get_dragon_cards() -> List[DragonCard]:
           Returns the list of DragonCard objects.
       set_dragon_cards(dragon_cards: List[DragonCard]) -> None:
           Sets the list of DragonCard objects.
       load_data() -> None:
           Loads the DragonCard objects from the configuration string and
           creates a shuffled list of AnimalDragonCard and PirateDragonCard objects.
    """
    def __init__(self, dragon_card_config_data: List[dict]):
        self._config_data = dragon_card_config_data
        self._dragon_cards: List[DragonCard] = []
        self.load_data()

    def get_dragon_cards(self) -> List[DragonCard]:
        """
        The get_dragon_cards function returns a list of DragonCard objects.


        :param self: Represent the instance of the class
        :return: A list of dragon cards
        """
        return self._dragon_cards

    def to_json_format(self) -> List[dict]:
        return [{"value": card.value, "character": card.character.name} for card in self._dragon_cards]

    def set_dragon_cards(self, dragon_cards: List[DragonCard]) -> None:
        """
        The set_dragon_cards function takes a list of DragonCard objects and sets the _dragon_cards attribute to that list.


        :param self: Refer to the instance of the class
        :param dragon_cards: List[DragonCard]: Set the dragon_cards attribute of the dragoncards class
        :return: None
        """
        self._dragon_cards = dragon_cards

    def load_data(self) -> None:
        """
        The load_data function is responsible for loading the data from the config file.
        It will split each line of the config file into a list, and then iterate through that list to create DragonCard objects.
        The function will also shuffle those cards before returning them.

        :param self: Refer to the current instance of a class
        :return: A list of dragoncard objects
        """
        dragon_cards: List[DragonCard] = []
        for dragon in self._config_data:
            value, character = dragon["value"], dragon["character"]
            if character == CharacterImage.PIRATE.name:
                dragon_cards.append(PirateDragonCard(CharacterImage[character], int(value)))
            else:
                dragon_cards.append(AnimalDragonCard(CharacterImage[character], int(value)))

        random.shuffle(dragon_cards)
        self._dragon_cards = dragon_cards
