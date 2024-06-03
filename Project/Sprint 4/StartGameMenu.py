from typing import Tuple
from Drawable import Drawable
import pygame
from GameConstants import GameStyles,GameElementStyles
import pygame_menu
from Player import Player
class StartGameMenu:
    def __init__(self,colour=GameStyles.COLOR_BROWN_DARK.value,games=[]):
        pygame.init()
        self.player_number = None
        self.screen_width, self.screen_height = pygame.display.get_desktop_sizes()[0]
        self.start_game_surface: pygame.Surface = pygame.Surface((self.screen_width, self.screen_height),
                                                                pygame.SRCALPHA)
        pygame.draw.rect(self.start_game_surface, colour, self.start_game_surface.get_rect(),
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        self.games = games#.get_previous_games()

        menu_theme = pygame_menu.themes.THEME_ORANGE
        # -------------------------------------------------------------------------
        # Create new game menu
        # -------------------------------------------------------------------------

        new_game_menu = pygame_menu.Menu(
            height = self.screen_height*0.7,
            theme = menu_theme,
            title = "New Game",
            width = self.screen_width*0.7
        )

        new_game_menu.add.selector('Select Number of Players',
                                   [1,2,3,4],
                                   theme=menu_theme,
                                   onchange = self.change_player_number,
                                   selector_id='select_No_players')
        new_game_menu.add.button('Start Game', self.start_game)

    # -------------------------------------------------------------------------
    # Create previous Game menu
    # -------------------------------------------------------------------------
        previous_game_menu = pygame_menu.Menu(
            height = self.screen_height*0.7,
            theme = menu_theme,
            title = "Previous Game",
            width = self.screen_width*0.7
        )
        for pg in self.games:
            previous_game_menu.add.button(pg, self.load_game)

        # -------------------------------------------------------------------------
        # Create main menu
        # -------------------------------------------------------------------------

        main_start_game_menu = pygame_menu.Menu(
            height = self.screen_height*0.7,
            theme=menu_theme,
            title = "Hydragons inspired by Fiery Dragons",
            width = self.screen_width*0.7
        )
        main_start_game_menu.add.button('New Game', new_game_menu)
        main_start_game_menu.add.button('previous Game', previous_game_menu)
        main_start_game_menu.add.button('Quit', pygame_menu.events.EXIT)



    def change_player_number(self, player_number):
        self.player_number = player_number

    def get_player_number(self):
        return self.player_number

    def start_game(self):
        pass
    def load_game(self):
        pass

if __name__ == "__main__":
    start_game_menu = StartGameMenu()
    start_game_menu.main_start_game_menu.mainloop(start_game_menu.start_game_surface)