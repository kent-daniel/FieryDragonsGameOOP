import pygame
from enum import Enum


class CharacterImage(Enum):
    BAT = 'Assets/BabyBat.png'
    DRAGON = 'Assets/BabyDragon.png'
    SPIDER = 'Assets/BabySpider.png'
    SALAMANDER = 'Assets/Salamander.png'


class GameImage(Enum):
    CAVE = 'Asset/cave.png'
    VOLCANO_ARENA = 'Asset/VolcanoArena.png'


class GameStyles(Enum):
    COLOR_RED = pygame.Color(255, 0, 0)
    COLOR_BROWN = pygame.Color(139, 69, 19)
    COLOR_BLUE = pygame.Color(0, 0, 255)
    COLOR_TRANSPARENT = pygame.Color(0, 0, 0, 0)

    BORDER_RADIUS_SMALL = 5
    BORDER_RADIUS_MEDIUM = 10
    BORDER_RADIUS_LARGE = 20

    FONT_SIZE_SMALL = 16
    FONT_SIZE_MEDIUM = 24
    FONT_SIZE_LARGE = 32