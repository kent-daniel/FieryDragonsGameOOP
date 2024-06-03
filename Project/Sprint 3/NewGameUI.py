from typing import Tuple
import pygame
from GameConstants import GameStyles, GameElementStyles
from Drawable import Drawable


class NewGameUI(Drawable):
    def __init__(self, height=GameElementStyles.SCREEN_HEIGHT.value, width=GameElementStyles.SCREEN_WIDTH.value,
                 input_height=GameElementStyles.RECT_HEIGHT_SMALL.value,
                 input_width=GameElementStyles.RECT_WIDTH_SMALL.value,
                 surface_colour=GameStyles.COLOR_BROWN_LIGHT.value, input_colour=GameStyles.COLOR_BROWN_DARK.value):
        spacing = input_width + input_height / 5
        self.new_game_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.text_1 = 'player 1:'
        self.input_box_1 = pygame.Rect(width // 2 - input_width - spacing, height // 2 - input_height - spacing // 2,
                                       input_width, input_height)
        self.text_2 = ''
        self.input_box_2 = pygame.Rect(width // 2 - input_width - spacing, height // 2 + spacing // 2,
                                       input_width, input_height)
        self.text_3 = ''
        self.input_box_3 = pygame.Rect(width // 2 - input_width - spacing, height // 2 + spacing + input_height,
                                       input_width, input_height)
        self.text_4 = ''
        self.input_box_4 = pygame.Rect(width // 2 - input_width - spacing,
                                       height // 2 - input_height * 2 - spacing // 2 - spacing,
                                       input_width, input_height)
        self.text_5 = 'Age:'
        self.input_box_5 = pygame.Rect(width // 2 + spacing, height // 2 - input_height - spacing // 2,
                                       input_width, input_height)
        self.text_6 = ''
        self.input_box_6 = pygame.Rect(width // 2 + spacing, height // 2 + spacing // 2,
                                       input_width, input_height)
        self.text_7 = ''
        self.input_box_7 = pygame.Rect(width // 2 + spacing, height // 2 + spacing + input_height,
                                       input_width, input_height)
        self.text_8 = ''
        self.input_box_8 = pygame.Rect(width // 2 + spacing, height // 2 - input_height * 2 - spacing // 2 - spacing,
                                       input_width, input_height)

        pygame.draw.rect(self.new_game_surface, surface_colour, self.new_game_surface.get_rect())
        pygame.draw.rect(self.new_game_surface, input_colour,
                         self.input_box_1,
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        pygame.draw.rect(self.new_game_surface, input_colour,
                         self.input_box_2,
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        pygame.draw.rect(self.new_game_surface, input_colour,
                         self.input_box_3,
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        pygame.draw.rect(self.new_game_surface, input_colour,
                         self.input_box_4,
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        pygame.draw.rect(self.new_game_surface, input_colour,
                         self.input_box_5,
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        pygame.draw.rect(self.new_game_surface, input_colour,
                         self.input_box_6,
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        pygame.draw.rect(self.new_game_surface, input_colour,
                         self.input_box_7,
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        pygame.draw.rect(self.new_game_surface, input_colour,
                         self.input_box_8,
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)

        self.rect: pygame.Rect = self.new_game_surface.get_rect()
        self.redraw_view()

    def draw(self, destination_surface: pygame.Surface, location=GameElementStyles.TOP_LEFT.value):
        self.redraw_view()
        self.rect.topleft = location
        destination_surface.blit(self.new_game_surface, self.rect.topleft)

    def get_surface(self):
        pass

    def redraw_view(self) -> None:
        font = pygame.font.SysFont(None, GameStyles.FONT_SIZE_LARGE.value)
        self.process_text() #todo make sure each text is correctly assigned based on input
        text1 = font.render(self.text_1, True, GameStyles.COLOR_BLACK.value)
        self.new_game_surface.blit(text1, (self.input_box_1.x + 5, self.input_box_1.y + 5))
        text2 = font.render(self.text_2, True, GameStyles.COLOR_BLACK.value)
        self.new_game_surface.blit(text2, (self.input_box_2.x + 5, self.input_box_2.y + 5))
        text3 = font.render(self.text_3, True, GameStyles.COLOR_BLACK .value)
        self.new_game_surface.blit(text3, (self.input_box_3.x + 5, self.input_box_3.y + 5))
        text4 = font.render(self.text_4, True, GameStyles.COLOR_BLACK.value)
        self.new_game_surface.blit(text4, (self.input_box_4.x + 5, self.input_box_4.y + 5))
        text5 = font.render(self.text_5, True, GameStyles.COLOR_BLACK.value)
        self.new_game_surface.blit(text5, (self.input_box_5.x + 5, self.input_box_5.y + 5))
        text6 = font.render(self.text_6, True, GameStyles.COLOR_BLACK.value)
        self.new_game_surface.blit(text6, (self.input_box_6.x + 5, self.input_box_6.y + 5))
        text7 = font.render(self.text_7, True, GameStyles.COLOR_BLACK.value)
        self.new_game_surface.blit(text7, (self.input_box_7.x + 5, self.input_box_7.y + 5))
        text8 = font.render(self.text_8, True, GameStyles.COLOR_BLACK.value)
        self.new_game_surface.blit(text8, (self.input_box_8.x + 5, self.input_box_8.y + 5))

    def process_text(self):
        pass