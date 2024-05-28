import unittest
from collections import deque
from typing import List
from unittest.mock import Mock
import pygame
from MovementEventManager import IMovementEventManager, IMovementEventListener
from GameDataController import IPlayerDataController
from Player import Player
from Square import Square
from GameConstants import CharacterImage
from Cave import Cave
from Movement import Movement
from PlayerMoveController import IPlayerMoveController, PlayerMoveController
from DragonCard import AnimalDragonCard, PirateDragonCard

pygame.init()
pygame.display.set_mode(pygame.display.get_desktop_sizes()[0], pygame.RESIZABLE)


def generate_mock_data() -> (List[Square], List[Player]):
    player1 = Player(1, 10)
    player2 = Player(2, 10)
    square0 = Square(0, CharacterImage.SALAMANDER)
    square1 = Square(1, CharacterImage.BABY_DRAGON, Cave(player1))
    square1.set_occupant(player1)
    square2 = Square(2, CharacterImage.SPIDER)
    square3 = Square(3, CharacterImage.BAT)
    square3.set_occupant(player2)
    square0.next = square1
    square1.prev = square0
    square1.next = square2
    square2.prev = square1
    square2.next = square3
    square3.prev = square2
    mock_squares = [square0, square1, square2, square3]
    mock_players = [player1, player2]

    return mock_squares, mock_players


class MockPlayerDataController(IPlayerDataController):
    def __init__(self):
        self._squares = []

    def get_players(self) -> deque[Player]:
        pass

    def set_players(self, players: deque[Player]) -> None:
        pass

    def get_num_volcanoes(self) -> int:
        pass

    def get_squares(self) -> List[Square]:
        return self._squares

    def set_squares(self, squares: List[Square]) -> None:
        self._squares = squares


class MockMovementManager(IMovementEventManager):

    def add_listener(self, listener: IMovementEventListener) -> None:
        pass

    def remove_event_listener(self, listener: IMovementEventListener) -> None:
        pass

    def publish_event(self, movement: Movement) -> None:
        print("published movement: ", movement.value, movement.destination.id)


class PlayerMoveControllerTest(unittest.TestCase):

    def setUp(self):
        self.mock_squares, self.mock_players = generate_mock_data()
        self.mock_data_controller: IPlayerDataController = MockPlayerDataController()
        self.mock_data_controller.set_squares(self.mock_squares)
        self.mock_event_publisher = Mock(wraps=MockMovementManager())
        self.player_move_controller: IPlayerMoveController = PlayerMoveController(self.mock_event_publisher,
                                                                                  self.mock_data_controller)

    def test_should_get_player_location(self):
        print("test_should_get_player_location")
        square = self.player_move_controller.get_player_location(self.mock_players[0])
        self.assertEqual(square, self.mock_squares[1])

    def test_should_not_move_to_occupied_square(self):
        print("test_should_not_move_to_occupied_square")
        # Given
        card = AnimalDragonCard(CharacterImage.BABY_DRAGON, 2)
        player = self.mock_players[0]

        # Action
        self.player_move_controller.process_movement(player, card)

        # Assert
        self.assertEqual(self.mock_squares[3].get_occupant(), self.mock_players[1])
        self.assertEqual(self.mock_squares[1].get_occupant(), self.mock_players[0])

    def test_should_not_move_pass_cave(self):
        print("test_should_not_move_pass_cave")
        # Given
        card = PirateDragonCard(CharacterImage.PIRATE, 1)

        # Action
        self.player_move_controller.process_movement(self.mock_players[0], card)

        # Assert
        self.assertEqual(self.mock_squares[0].get_occupant(), None)
        self.assertEqual(self.mock_squares[1].get_occupant(), self.mock_players[0])

    def test_should_move_forward(self):
        print("test_should_move_forward")
        # Given
        card = AnimalDragonCard(CharacterImage.BABY_DRAGON, 1)

        # Action
        self.player_move_controller.process_movement(self.mock_players[0], card)

        # Assert
        self.assertEqual(self.mock_squares[1].get_occupant(), None)
        self.assertEqual(self.mock_squares[2].get_occupant(), self.mock_players[0])

    def test_should_move_backward(self):
        print("test_should_move_backward")
        # Given
        card = PirateDragonCard(CharacterImage.PIRATE, 1)

        # Action
        self.player_move_controller.process_movement(self.mock_players[1], card)

        # Assert
        self.assertEqual(self.mock_squares[3].get_occupant(), None)
        self.assertEqual(self.mock_squares[2].get_occupant(), self.mock_players[1])


if __name__ == '__main__':
    unittest.main()
