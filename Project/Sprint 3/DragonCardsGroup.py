import time
from typing import Tuple, Optional
from NotificationManager import NotificationManager
import pygame

from GameConstants import GameImage, GameStyles, GameElementStyles
from DragonCard import DragonCard
from GameDataController import IDragonCardDataController
from Drawable import Drawable
from MovementEventManager import IMovementEventListener
from Movement import Movement


class DragonCardsGroup(Drawable, IMovementEventListener):
    """
    DragonCardsGroup

    Authored by: Vansh Batas

    This class represents a group of DragonCard objects displayed in a game area.
    It implements the Drawable and IMovementEventListener interfaces, allowing it to be drawn
    on a surface and respond to movement events.

    Methods:
       __init__(data_controller: IDragonCardDataController, width: int = GameElementStyles.DRAGON_CARD_AREA_HEIGHT.value,
                height: int = GameElementStyles.DRAGON_CARD_AREA_HEIGHT.value, arena_image: str = GameImage.VOLCANO_ARENA.value,
                notification_manager=NotificationManager()) -> None:
           Initializes the DragonCardsGroup with a data controller, dimensions, arena image, and a notification manager.
       draw(destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
           Draws the DragonCardsGroup on a destination surface at a given location.
       get_clicked_card(mouse_pos: (int, int)) -> Optional[DragonCard]:
           Returns the DragonCard object clicked by the mouse, or None if no card was clicked.
       redraw_view() -> None:
           Redraws the view of the DragonCardsGroup.
       _draw_dragon_cards() -> None:
           Draws the DragonCard objects on the group's surface.
       get_surface() -> pygame.Surface:
           Returns the surface of the DragonCardsGroup.
       on_movement_event(movement: Movement) -> None:
           Handles a movement event (not implemented in the provided code).
    """
    def __init__(self, data_controller: IDragonCardDataController,
                 width: int = GameElementStyles.DRAGON_CARD_AREA_HEIGHT.value,
                 height: int = GameElementStyles.DRAGON_CARD_AREA_HEIGHT.value,
                 arena_image: str = GameImage.VOLCANO_ARENA.value,
                 notification_manager=NotificationManager()):
        """
        The __init__ function is called when the class is instantiated.
        It sets up all of the instance variables that are needed for this object to function properly.
        The self parameter refers to the instance of this class, and allows us to access its attributes and methods.

        :param self: Refer to the current instance of the class
        :param data_controller: IDragonCardDataController: Pass the data controller to the view
        :param width: int: Set the width of the dragon card area
        :param height: int: Set the height of the dragon card area
        :param arena_image: str: Load the image of the arena
        :param notification_manager: Send notifications to the game controller
        :return: Nothing
        """
        self._data_controller = data_controller
        self._notification_manager = notification_manager
        self._dragon_cards = self._data_controller.get_dragon_cards()
        self._width = width
        self._height = height
        self._image: pygame.Surface = pygame.image.load(arena_image).convert_alpha()
        self._image = pygame.transform.smoothscale(self._image, (self._width, self._height))
        self._surface: pygame.Surface = pygame.Surface((self._width, self._height), pygame.SRCALPHA)
        pygame.draw.rect(self._surface,
                         GameStyles.COLOR_TRANSPARENT.value,
                         self._surface.get_rect(),
                         )
        self._surface.blit(self._image, self._image.get_rect(
            center=self._surface.get_rect().center))
        self._rect = self._surface.get_rect()
        self.redraw_view()

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        """
        The draw function is responsible for drawing the view to a surface.
        It takes two arguments:
            destination_surface - The surface that the view will be drawn on.
            location - A tuple containing an x and y coordinate representing where the center of this view should be drawn.

        :param self: Refer to the object itself
        :param destination_surface: pygame.Surface: Specify the surface that the view will be drawn to
        :param location: Tuple[int: Specify the location of the sprite
        :param int]: Define the location of the view on the screen
        :return: None
        """
        self.redraw_view()
        self._rect.center = location
        destination_surface.blit(self._surface, self._rect.topleft)

    def get_clicked_card(self, mouse_pos: (int, int)) -> Optional[DragonCard]:
        """
        The get_clicked_card function takes in a mouse_pos tuple and returns the DragonCard that was clicked on.
        If no card is clicked, it returns None.

        :param self: Access the instance of the class
        :param mouse_pos: (int: Determine the position of the mouse on screen
        :param int): Get the x and y coordinates of the mouse position
        :return: The card that was clicked
        """
        for i in range(len(self._dragon_cards)):
            card = self._dragon_cards[i]
            # Calculate the mouse position for proper click detection.
            relative_mouse_pos = (mouse_pos[0] - self._rect.x - card.get_surface().get_width() // 2,
                                  mouse_pos[1] - self._rect.y - card.get_surface().get_height() // 2)
            if card.is_clicked(relative_mouse_pos):
                self._dragon_cards[i] = card
                self._notification_manager.add_notification(f"card flipped: {card.value} x {card.character.name}")
                self.redraw_view()
                return self._dragon_cards[i]
        return None

    def redraw_view(self) -> None:
        """
        The redraw_view function is called when the view needs to be redrawn.
        This function will call the draw_dragon_cards function, which will then
        call the draw_card function for each card in self._dragon_cards.

        :param self: Refer to the object that is calling the function
        :return: None
        """
        self._draw_dragon_cards()

    def _draw_dragon_cards(self) -> None:
        """
        The _draw_dragon_cards function draws the dragon cards on the screen.

        :param self: Refer to the object itself
        :return: None
        """
        gap = 5
        startx = self._width * 0.15
        starty = 0
        card_width = self._dragon_cards[0].get_surface().get_width() if self._dragon_cards else 0
        num_row_cards = int((self._width * 0.8) // card_width) if card_width > 0 else 1

        for i, card in enumerate(self._dragon_cards):
            if i % num_row_cards == 0:
                startx = self._width * 0.15  # Reset x-coordinate for new row
                starty += card.get_surface().get_height() + gap  # Move to next row

            card.draw(self._surface, (startx, starty))

            startx += card_width + gap

    def get_surface(self) -> pygame.Surface:
        """
        The get_surface function returns the surface of the object.

        :param self: Refer to the object itself
        :return: The surface of the object
        """
        return self._surface

    def on_movement_event(self, movement: Movement) -> None:
        """
        The on_movement_event function is called whenever a movement event occurs.
        A movement event is when the player moves from one room to another, or when they move within a room.
        The function takes in an argument of type Movement, which contains information about the movement that occurred.

        :param self: Refer to the object itself
        :param movement: Movement: Get the movement of the player
        :return: None
        """
        pass
