import math
from typing import List, Tuple

import pygame.sprite
from Square import Square
from VolcanoCard import VolcanoCard
from GameConstants import CharacterImage, GameStyles
from Player import Player
from Cave import Cave



class Board(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, square_animals: List[str], volcano_size: int, square_size: int,
                 color: pygame.color = GameStyles.COLOR_GRAY_500.value):
        super().__init__()
        self.width = width
        self.height = height
        self.radius = 0
        self.squares: List[Square] = self.create_linked_squares(square_animals, square_size)
        self.volcanoes: List[VolcanoCard] = self.create_volcano_cards(self.squares, volcano_size, square_size)
        self.board_surface: pygame.Surface = pygame.Surface((width, height), pygame.SRCALPHA)

        pygame.draw.rect(self.board_surface, color, self.board_surface.get_rect())
        self.rect: pygame.Rect = self.board_surface.get_rect()
        self.draw_volcano_cards(self.volcanoes, self.radius)

    def create_linked_squares(self, square_animals: List[str], square_size: int) -> List[Square]:

        players = [Player(1, GameStyles.COLOR_BLUE.value), Player(2, GameStyles.COLOR_ORANGE.value), Player(3, GameStyles.COLOR_PINK.value), Player(4, GameStyles.COLOR_PURPLE.value)]
        squares = [
            Square(1, CharacterImage.BAT), Square(2, CharacterImage.SPIDER, cave=Cave(cave_owner=players[0])),
            Square(3, CharacterImage.SALAMANDER),
            Square(4, CharacterImage.SPIDER), Square(5, CharacterImage.BAT), Square(6, CharacterImage.SPIDER),
            Square(7, CharacterImage.SALAMANDER), Square(8, CharacterImage.BABY_DRAGON, cave=Cave(cave_owner=players[1])), Square(9, CharacterImage.BAT),
            Square(10, CharacterImage.BAT), Square(11, CharacterImage.BABY_DRAGON),
            Square(12, CharacterImage.SALAMANDER),
            Square(13, CharacterImage.BABY_DRAGON), Square(14, CharacterImage.SPIDER , cave=Cave(cave_owner=players[2])),
            Square(15, CharacterImage.BABY_DRAGON),
            Square(16, CharacterImage.SALAMANDER), Square(17, CharacterImage.BAT),
            Square(18, CharacterImage.SALAMANDER),
            Square(19, CharacterImage.BABY_DRAGON), Square(20, CharacterImage.BAT , cave=Cave(cave_owner=players[3])), Square(21, CharacterImage.BAT),
            Square(22, CharacterImage.BABY_DRAGON), Square(23, CharacterImage.SALAMANDER),
            Square(24, CharacterImage.BAT)
        ]
        # Link the squares together to form a doubly linked list
        for i in range(len(squares) - 1):
            squares[i].next = squares[i + 1]
            squares[i + 1].prev = squares[i]
        return squares

    def create_volcano_cards(self, squares: List[Square], volcano_size: int, square_size: int, padding: int = 10) -> \
    List[VolcanoCard]:
        num_volcanoes = len(squares) // volcano_size
        volcanoes = []
        for i in range(num_volcanoes):
            start_index = i * volcano_size
            end_index = start_index + volcano_size
            card_squares = squares[start_index:end_index]
            # for c in card_squares:
            #     print(c.character)

            self.radius = self.width * 0.5 - 2 * square_size - 30
            volcano_width = self.get_optimal_volcano_width(board_radius=int(self.radius),
                                                           central_angle=360 / num_volcanoes)
            total_volcano_width = volcano_width + (volcano_size - 1) * padding
            total_volcano_height = square_size + 2 * padding
            volcanoes.append(VolcanoCard(card_squares, total_volcano_width, total_volcano_height, padding))
        return volcanoes

    def draw(self, destination_surface: pygame.Surface, location: Tuple[int, int]) -> None:
        self.rect.center = location
        destination_surface.blit(self.board_surface, self.rect.topleft)

    def get_optimal_volcano_width(self, board_radius: int, central_angle: float) -> int:
        central_angle_rad = math.radians(central_angle)
        # Calculate the minimum side length using the apothem length (using board radius) and central angle
        side_length = 2 * board_radius * math.tan(central_angle_rad / 2)
        return int(side_length)

    def draw_volcano_cards(self, volcano_cards: List[VolcanoCard], radius: int) -> None:
        apothem = radius
        central_angle = 360 / len(volcano_cards)
        rotation_degrees = 0
        for volcano in volcano_cards:
            volcano.rotate(rotation_degrees)

            # Calculate card center coordinate based on screen center and apothem
            card_center = (
                int(self.board_surface.get_rect().centerx + apothem * math.cos(math.radians(rotation_degrees))),
                int(self.board_surface.get_rect().centery - apothem * math.sin(math.radians(rotation_degrees)))
            )
            volcano.draw(self.board_surface, card_center)
            rotation_degrees += central_angle
