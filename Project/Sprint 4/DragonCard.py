from abc import ABC, abstractmethod
from typing import Tuple
from Square import Square
from Player import Player
import pygame
from GameConstants import CharacterImage
from Drawable import Drawable
from GameConstants import GameStyles
from Movement import Movement
from CardEffectsController import CardEffectsController

UNFLIP_EVENT = pygame.USEREVENT + 1
FLIP_TIME = 1000


class DragonCard(Drawable, ABC):
    """
    DragonCard

    Authored by: Vansh Batas

    This abstract base class defines a card object for a game. It manages the card's state,
    including whether it is flipped or not, its value, and its associated character image.
    It also provides methods for drawing the card on a surface.

    Methods:
       __init__(character: CharacterImage, value: int, is_flipped: bool = False, radius: int = 45) -> None:
           Initializes the card with a character image, value, flipped state, and radius.
       unflip() -> None:
           Unflips the card and updates the surface.
       flip() -> int:
           Flips the card and updates the surface. Returns the time when the card was flipped.
       is_clicked(mouse_pos: Tuple[int, int]) -> bool:
           Checks if the mouse is clicked on the card and flips the card if so.
       redraw_view() -> None:
           Redraws the card's surface based on its current state (flipped or not).
       draw(destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
           Draws the card's surface on a destination surface at a given location.
       get_surface() -> pygame.Surface:
           Returns the card's surface.
       @property character() -> CharacterImage:
           Returns the character image associated with the card.
       @property value() -> int:
           Returns the value of the card.
       @abstractmethod action(square: Square) -> Movement:
           An abstract method that subclasses must implement to define the card's action when played.
    """

    def __init__(self, character: CharacterImage, effect_controller: CardEffectsController, value: int,
                 is_flipped: bool = False, radius: int = 45):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the initial state of the object.
        The self parameter refers to an instance of a class, and is used to access variables that belong to the class.

        :param self: Refer to the object itself
        :param character: CharacterImage: Store the image of the character
        :param value: int: Store the value of the card
        :param is_flipped: bool: Determine if the card is flipped or not
        :param radius: int: Set the size of the card
        :return: The self
        """
        self._character = character
        self._effect_controller = effect_controller
        self._value = value
        self._character = character
        self._radius = radius
        self._is_flipped = is_flipped
        self._flip_time = None  # To store the time when the card was flipped
        self._image: pygame.Surface = pygame.image.load(self._character.value).convert_alpha()
        self._image = pygame.transform.smoothscale(self._image, (self._radius * 0.8, self._radius * 0.8))
        self._surface: pygame.Surface = pygame.Surface((self._radius * 2, self._radius * 2), pygame.SRCALPHA)
        self._rect: pygame.Rect = self._surface.get_rect()
        self.redraw_view()

    def unflip(self):
        """
        The unflip function is used to unflip the card.
        It sets the _is_flipped attribute to False and calls redraw_view()

        :param self: Refer to the object itself
        :return: Nothing
        """
        self._is_flipped = False
        self.redraw_view()

    def flip(self):
        """
        The flip function is used to update the screen with whatever you've drawn.
        This function will update the contents of the entire display. If your program has changed (or set)
        the contents of individual pixels, but not called flip(), those changes will not be visible until this function is called.

        :param self: Refer to the object itself
        :return: The time at which the card was flippe
        """
        self._is_flipped = True
        self._flip_time = pygame.time.get_ticks()
        self.redraw_view()

    def is_clicked(self, mouse_pos: Tuple[int, int]) -> bool:
        """
        The is_clicked function checks if the mouse is clicked on a card.
        If it is, then the card flips and returns True. If not, then it returns False.

        :param self: Refer to the object itself
        :param mouse_pos: Tuple[int: Determine the position of the mouse, int: Determine the position of the mouse]
        :return: A boolean value
        """
        if self._rect.collidepoint(mouse_pos):
            self.flip()
            return True
        return False

    def redraw_view(self):
        """
        The redraw_view function is called when the view needs to be redrawn and it is also responsible for the flipping logic of the dragon cards.
        This function will draw a circle with a radius of self._radius and fill it with GameStyles.COLOR_BROWN_LIGHT.value,
        which is defined in the GameStyles class as (255, 255, 0). The circle will be drawn at coordinates (self._radius, self._radius)
        on the surface object that was passed into this class's constructor.

        :param self: Refer to the object itself
        :return: A surface with a circle, text and an imag
        """
        self._surface.fill(GameStyles.COLOR_TRANSPARENT.value)
        # Draw dragon card if it is flipped.
        if self._is_flipped:
            pygame.draw.circle(self._surface, GameStyles.COLOR_PINK.value, (self._radius, self._radius), self._radius)
            font = pygame.font.SysFont(None, GameStyles.FONT_SIZE_LARGE.value)
            text = font.render(str(self._value), True, GameStyles.COLOR_GRAY_700.value)
            text_rect = text.get_rect(center=(self._surface.get_rect().centerx, self._surface.get_rect().top + 15))
            self._surface.blit(text, text_rect)
            self._surface.blit(self._image, self._image.get_rect(center=self._surface.get_rect().center))
        # Draw the unflipped dragon card surface.
        else:
            pygame.draw.circle(self._surface, GameStyles.COLOR_BROWN_LIGHT.value, (self._radius, self._radius),
                               self._radius)

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        """
        The draw function takes a destination surface and location as parameters.
        The card's image is blitted to the destination surface at the given location.
        If the card has been flipped, it will unflip after 1 second.

        :param self: Access the object's attributes and methods
        :param destination_surface: pygame.Surface: Draw the card on a surface
        :param location: Tuple[int: Determine where the card will be drawn on the screen
        :param int]: Set the location of the card on the screen
        :return: None, because it is a void function
        """
        if self._flip_time and pygame.time.get_ticks() - self._flip_time >= FLIP_TIME:  # Check if 1 second has passed since the card was flipped
            self.unflip()
        self._rect.center = location
        destination_surface.blit(self._surface, self._rect.center)

    def get_surface(self) -> pygame.Surface:
        """
        The get_surface function returns the surface of the object.

        :param self: Access the attributes and methods of the class
        :return: A surface
        """
        return self._surface

    @property
    def character(self) -> CharacterImage:
        """
        The character function returns the character image of the current state.


        :param self: Represent the instance of the class
        :return: The character image of the object
        """
        return self._character

    @property
    def value(self) -> int:
        """
        The value function returns the value of a card.

        :param self: Represent the instance of the class
        :return: The value of the card
        """
        return self._value

    @abstractmethod
    def action(self, player):
        """
        The action function is the main function of your agent. It takes a single argument, square, which is a Square
        object representing the state of the board at that moment in time. The action function must return an instance
        of Movement.

        :param self: Refer to the current instance of a class
        :param square: Square: Get information about the current square
        :return: A movement object
        """
        pass


class AnimalDragonCard(DragonCard):
    """
    AnimalDragonCard

    Authored by: Vansh Batas

    This class represents an animal-themed card in the game. It inherits from the DragonCard class
    and implements the action method to move a character forward on the game board.

    Methods:
       __init__(character: CharacterImage, value: int, is_flipped: bool = False, radius: int = 30) -> None:
           Initializes the AnimalDragonCard with a character image, value, flipped state, and radius.
       action(square: Square) -> Movement:
           Moves the character on the given square forward by the value of the card.
    """

    def __init__(self, character: CharacterImage, value: int, is_flipped: bool = False):
        """
        The __init__ function is called when the object is created.
        It sets up the initial state of the object.
        The __init__ function takes in a character, value, and radius as parameters.

        :param self: Represent the instance of the object itself
        :param character: CharacterImage: Set the character image to be used for the card
        :param value: int: Set the value of a card
        :param is_flipped: bool: Determine whether the card is flipped or not
        :param radius: int: Set the radius of the circle
        :return: A new card object
        """
        super().__init__(character, value, is_flipped)

    def action(self, player: Player):
        """
        The action function takes a square as an argument and returns a movement.
        The movement is the number of squares to move, and the destination square.
        If there is no character on the given square, then return 0 for both values.
        Otherwise, if there is a character on that square:

        :param self: Refer to the object itself
        :param square: Square: Get the square that is being moved to
        :return: A movement object, which is a namedtuple that contains the value of the card and the destination square
        """
        super()._effect_controller.animal_effect(self, player)


class PirateDragonCard(DragonCard):
    """
    PirateDragonCard

    Authored by: Vansh Batas

    This class represents a pirate-themed card in the game. It inherits from the DragonCard class
    and implements the action method to move a character backward on the game board.

    Methods:
       __init__(character: CharacterImage, value: int, is_flipped: bool = False, radius: int = 30) -> None:
           Initializes the PirateDragonCard with a character image, value, flipped state, and radius.
       action(square: Square) -> Movement:
           Moves the character on the given square backward by the value of the card.
    """

    def __init__(self, character: CharacterImage, value: int, is_flipped: bool = False):
        """
        The __init__ function is called when the object is created.
        It sets up the initial state of the object.
        The __init__ function takes in a character, value, and radius as parameters.

        :param self: Represent the instance of the object itself
        :param character: CharacterImage: Set the character image of the card
        :param value: int: Set the value of the card
        :param is_flipped: bool: Determine if the card is flipped or not
        :return: The super class, which is a card
        """
        super().__init__(character, value, is_flipped)

    def action(self, player: Player):
        """
        The action function takes a square as an argument and returns a movement.
        The movement is the number of squares to move backwards, and the destination
        square.

        :param self: Access the attributes of the class
        :param square: Square: Get the square that is being moved from
        :return: A movement object
        """
        super()._effect_controller.pirate_effect(self, player)


class SpecialDragonCard(DragonCard):
    def __init__(self, character: CharacterImage, value: int, is_flipped: bool = False):
        super().__init__(character, value, is_flipped)

    def action(self, player: Player):
        self._effect_controller.special_effect(self, player)
