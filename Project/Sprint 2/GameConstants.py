import pygame
from enum import Enum


class CharacterImage(Enum):
    BAT = 'Assets/BabyBat.png'
    BABY_DRAGON = 'Assets/BabyDragon.png'
    SPIDER = 'Assets/BabySpider.png'
    SALAMANDER = 'Assets/Salamander.png'


class GameImage(Enum):
    CAVE = 'Assets/Cave.png'
    VOLCANO_ARENA = 'Assets/VolcanoArena.png'

class GameElementStyles(Enum):
    SQUARE_LENGTH = 75
    CAVE_SIZE = 70
    CAVE_OFFSET = 3

class GameStyles(Enum):
    COLOR_RED = pygame.Color(255, 100, 80)
    COLOR_BROWN = pygame.Color(153, 102, 51)
    COLOR_BLUE = pygame.Color(51, 153, 255)
    COLOR_PURPLE = pygame.Color(153, 102, 204)
    COLOR_ORANGE = pygame.Color(255, 153, 51)
    COLOR_PINK = pygame.Color(255, 153, 204)

    COLOR_TRANSPARENT = pygame.Color(0, 0, 0, 0)
    COLOR_GRAY_500 = pygame.Color(128, 128, 128)
    COLOR_GRAY_300 = pygame.Color(192, 192, 192)
    COLOR_GRAY_700 = pygame.Color(77, 77, 77)

    BORDER_RADIUS_SMALL = 5
    BORDER_RADIUS_MEDIUM = 10
    BORDER_RADIUS_LARGE = 20

    FONT_SIZE_SMALL = 16
    FONT_SIZE_MEDIUM = 24
    FONT_SIZE_LARGE = 32