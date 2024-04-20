from typing import List

import pygame.sprite
from Square import Square
from VolcanoCard import VolcanoCard
import GameConstants
class Board(pygame.sprite.Sprite):
    def __init__(self,width: int , height: int ,  square_animals: List[str], volcano_squares: int, square_size: int, num_volcanoes: int):
        super().__init__()
        self.volcanoes: List[VolcanoCard] = []
        self.squares: List[Square] = self.create_squares(square_animals,square_size)
        self.board_surface: pygame.Surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.board_surface,
                         GameConstants.GameStyles.COLOR_TRANSPARENT.value,
                         self.board_surface.get_rect(),
                         )
        self.rect: pygame.Rect = self.board_surface.get_rect()

    def create_squares(self, square_animals: List[str], square_size: int) -> List[Square]:
        return [Square(square_size, GameConstants.CharacterImage[animal].value) for animal in square_animals]
    # def draw_volcano_cards(self, volcano_size:int, square_size:int)-> None:

    #     for i in range(len(self.squares)):
    #         self.volcanoes.append(VolcanoCard(card_squares=[],width=volcano_size*square_size, height=volcano_size))
    #