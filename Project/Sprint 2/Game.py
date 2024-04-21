from collections import deque
from configparser import ConfigParser
from typing import List

import pygame
from Board import Board
from Player import Player




class Game:
    def __init__(self, config_path: str, screen: pygame.surface.Surface):
        self.config = ConfigParser()
        self.config.read(config_path)

        self.dragon_cards= pygame.sprite.Group()
        self.players: deque[Player] = deque()
        self.screen = screen
        self.board: Board = self.create_board(config=self.config, screen=self.screen)


    def create_board(self, config: ConfigParser, screen: pygame.surface.Surface) -> Board:
        square_animals : List[str] = [animal.strip(" ") for animal in config.get('GameConfig','square_animals').split(",")]
        volcano_size : int = int(config.get('GameConfig','volcano_size'))
        return Board(int(screen.get_width()*0.7),screen.get_height(),square_animals,volcano_size,70)
    def run_main_loop(self):
        pass

    def create_players(self):
        pass

    def quit(self) -> None:
        pygame.quit()
