import pygame
from enum import Enum
pygame.init()


class CharacterImage(Enum):
    BAT = 'Assets/BabyBat.png'
    BABY_DRAGON = 'Assets/BabyDragon.png'
    SPIDER = 'Assets/BabySpider.png'
    SALAMANDER = 'Assets/Salamander.png'
    PIRATE = 'Assets/Cave.png'


class GameImage(Enum):
    CAVE = 'Assets/Cave.png'
    VOLCANO_ARENA = 'Assets/VolcanoArena.png'


class GameElementStyles(Enum):
    """
    Author: Kent Daniel and Guntaj Singh
    """
    SQUARE_LENGTH = 75
    CAVE_SIZE = 70
    CAVE_OFFSET = 4
    PLAYER_HEIGHT = 35
    DRAGON_CARD_AREA_HEIGHT = 540
    PLAYER_STEPS_TO_WIN = 24
    SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_desktop_sizes()[0]
    RECT_WIDTH_SMALL, RECT_HEIGHT_SMALL = SCREEN_WIDTH / 8, SCREEN_HEIGHT / 8
    RECT_WIDTH_MEDIUM, RECT_HEIGHT_MEDIUM = SCREEN_WIDTH / 6, SCREEN_HEIGHT / 6
    RECT_WIDTH_LARGE, RECT_HEIGHT_LARGE = SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4
    TOP_LEFT = (0, 0)


class GameStyles(Enum):
    COLOR_BROWN_DARK = pygame.Color(70, 30, 10)
    COLOR_BROWN_LIGHT = pygame.Color(153, 102, 51)
    COLOR_BLUE = pygame.Color(51, 153, 255)
    COLOR_PURPLE = pygame.Color(153, 102, 204)
    COLOR_ORANGE = pygame.Color(255, 153, 51)
    COLOR_PINK = pygame.Color(255, 153, 204)

    COLOR_TRANSPARENT = pygame.Color(0, 0, 0, 0)
    COLOR_GRAY_500 = pygame.Color(128, 128, 128)
    COLOR_GRAY_300 = pygame.Color(192, 192, 192)
    COLOR_GRAY_700 = pygame.Color(77, 77, 77)
    COLOR_GRAY_700_T = pygame.Color(50, 50, 50, 190)
    COLOR_BLACK = pygame.Color(0, 0, 0)

    BORDER_RADIUS_SMALL = 5
    BORDER_RADIUS_MEDIUM = 10
    BORDER_RADIUS_LARGE = 20

    PADDING_SMALL = 10
    PADDING_MEDIUM = 20
    PADDING_LARGE = 30

    FONT_SIZE_SMALL = 16
    FONT_SIZE_MEDIUM = 24
    FONT_SIZE_LARGE = 32
    FONT_SIZE_WIN = 64
    FONT_WIN = 'freesansbold.ttf'
    screen_width, screen_height = pygame.display.get_desktop_sizes()[0]
