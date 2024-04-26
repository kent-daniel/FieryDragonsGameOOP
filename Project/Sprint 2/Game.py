from collections import deque
from configparser import ConfigParser
from typing import List

import pygame
from Board import Board
from Player import Player
from GameDataController import GameDataController
from DragonCardsGroup import DragonCardsGroup
from DragonCard import DragonCard
from PlayerMoveController import IPlayerMoveController , PlayerMoveController
from MovementEventManager import IMovementEventManager , MovementEventManager

class Game:
    def __init__(self, config_path: str,screen: pygame.surface.Surface):
        self._data_controller = GameDataController(config_path)
        self._board = Board(int(screen.get_width() * 0.7), screen.get_height(), self._data_controller)
        self._dragon_cards = DragonCardsGroup(self._data_controller.get_dragon_cards())
        self._movement_manager : IMovementEventManager= MovementEventManager()
        self._player_move_controller: IPlayerMoveController= PlayerMoveController(self._movement_manager, self._data_controller)
        self._movement_manager.add_listener(self._board)
        self._movement_manager.add_listener(self._dragon_cards)
        self._screen = screen
        self.render_game()

    def render_game(self):
        self._draw_dragon_cards()
        self._draw_board()
    def _draw_board(self):
        self._board.draw(self._screen, self._screen.get_rect().center)

    def _draw_dragon_cards(self):
        self._dragon_cards.draw(self._screen, self._screen.get_rect().center)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                card = self._dragon_cards.get_clicked_card(pygame.mouse.get_pos())
                if card:
                    self._handle_chosen_card(card)
    def _handle_chosen_card(self, card: DragonCard):
        print(card)
    def run_main_loop(self):
        pass

    def initialise_game(self):
        pass

    def quit(self) -> None:
        pygame.quit()
