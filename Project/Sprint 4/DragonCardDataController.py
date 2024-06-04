import random
from abc import ABC, abstractmethod
from typing import List
from DragonCard import DragonCard, PirateDragonCard, AnimalDragonCard, SpecialDragonCard
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
    def set_dragon_cards(self, dragon_cards: List[DragonCard]) ->None:
        """
        The set_dragon_cards function is used to set the dragon cards for a player.

        :param self: Represent the instance of the class
        :param dragon_cards: List[DragonCard]: Specify the type of data that is being passed into the function
        :return: None
        """
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
    def __init__(self, dragon_card_config_data: str):
        """
        The __init__ function is the constructor for a class. It is called when an object of that class
        is instantiated, and it sets up the attributes of that object. In this case, we are setting up
        the DragonCardManager with a string containing all of our dragon card data.

        :param self: Represent the instance of the class
        :param dragon_card_config_data: str: Pass in the data to be used by the class
        :return: None
        """
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

    def set_dragon_cards(self, dragon_cards: List[DragonCard]) ->None:
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
        dragons = self._config_data.split(",")
        dragon_cards: List[DragonCard] = []
        for dragon in dragons:
            value, character = dragon.split("x")
            if character == CharacterImage.PIRATE.name:
                dragon_cards.append(PirateDragonCard(CharacterImage[character], int(value)))
            elif character == CharacterImage.SPECIAL.name:
                dragon_cards.append(SpecialDragonCard(CharacterImage[character], int(value)))
            else:
                dragon_cards.append(AnimalDragonCard(CharacterImage[character], int(value)))

        random.shuffle(dragon_cards)
        self._dragon_cards = dragon_cards
