from collections import deque
from configparser import ConfigParser
from typing import List

import pygame
from Board import Board
from Player import Player
from GameDataController import GameDataController
from DragonCardsGroup import DragonCardsGroup


class Game:
    def __init__(self, config_path: str,screen: pygame.surface.Surface):
        data_controller = GameDataController(config_path)
        self._board = Board(int(screen.get_width() * 0.7), screen.get_height(), data_controller)
        self._dragon_cards = DragonCardsGroup(data_controller)
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
                    print(card)
    def run_main_loop(self):
        pass

    def create_players(self):
        pass

    def quit(self) -> None:
        pygame.quit()
