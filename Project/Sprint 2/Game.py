from collections import deque
from configparser import ConfigParser
from typing import List

import pygame
from Board import Board
from Player import Player
from GameDataController import GameDataController



class Game:
    def __init__(self, config_path: str, screen: pygame.surface.Surface):
        self.config = ConfigParser()
        self.config.read(config_path)

        self.dragon_cards= pygame.sprite.Group()
        self.players: deque[Player] = deque()
        self.screen = screen

        self.data_controller = GameDataController(config_path)
        self.board: Board = Board(int(screen.get_width()*0.7),screen.get_height(), self.data_controller)

    def run_main_loop(self):
        pass

    def create_players(self):
        pass

    def quit(self) -> None:
        pygame.quit()
