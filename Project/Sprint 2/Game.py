from collections import deque
from configparser import ConfigParser

import pygame
from Board import Board
from Player import Player




class Game:
    def __init__(self, config_path: str, screen: pygame.surface.Surface):
        self.dragon_cards= pygame.sprite.Group()
        self.board: Board or None = None
        self.players: deque[Player] = deque()

        self.screen = screen
        self.config = ConfigParser()
        self.config.read(config_path)

    def create_board(self) -> None:
        pass
    def run_main_loop(self):
        pass

    def create_players(self):
        pass

    def quit(self) -> None:
        pygame.quit()
