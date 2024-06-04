from typing import Tuple, Any
import pygame
from GameConstants import GameStyles
import pygame_menu
from GameDataController import GameDataController
from GameDataController import GameProgressData


class StartGameMenu:
    def __init__(self, game_data_controller: GameDataController, colour=GameStyles.COLOR_BROWN_DARK.value):
        self.main_start_game_menu = None
        pygame.init()
        self.player_number = 2
        self.colour = colour
        self.game_data_controller = game_data_controller
        self.screen_width, self.screen_height = pygame.display.get_desktop_sizes()[0]
        self.start_game_surface: pygame.Surface = pygame.Surface((self.screen_width, self.screen_height),
                                                                 pygame.SRCALPHA)
        pygame.draw.rect(self.start_game_surface, colour, self.start_game_surface.get_rect(),
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        self.games = self.game_data_controller.get_saved_games()

        self.menu_theme = pygame_menu.themes.THEME_ORANGE
        # -------------------------------------------------------------------------
        # Create new game menu
        # -------------------------------------------------------------------------

        self.new_game_menu = pygame_menu.Menu(
            height=self.screen_height * 0.7,
            theme=self.menu_theme,
            title="New Game",
            width=self.screen_width * 0.7
        )

        self.new_game_menu.add.selector('Select Number of Players',
                                        [('2', 2), ('3', 3), ('4', 4)],
                                        onchange=self.change_player_number,
                                        selector_id='select_No_players')
        self.new_game_menu.add.button('Start Game', self.start_game)

        # -------------------------------------------------------------------------
        # Create previous Game menu
        # -------------------------------------------------------------------------
        self.previous_game_menu = pygame_menu.Menu(
            height=self.screen_height * 0.7,
            theme=self.menu_theme,
            title="Previous Game",
            width=self.screen_width * 0.7
        )
        for pg in self.games:
            self.previous_game_menu.add.button(pg.time_saved, self.load_game, pg)

        # -------------------------------------------------------------------------
        # Create main menu
        # -------------------------------------------------------------------------

    def run_menu(self, surface):
        self.main_start_game_menu = pygame_menu.Menu(
            height=self.screen_height * 0.7,
            theme=self.menu_theme,
            title="Hydragons inspired by Fiery Dragons",
            width=self.screen_width * 0.7
        )
        self.main_start_game_menu.add.button('New Game', self.new_game_menu)
        self.main_start_game_menu.add.button('previous Game', self.previous_game_menu)
        self.main_start_game_menu.add.button('Quit', pygame_menu.events.EXIT)
        self.main_start_game_menu.enable()
        if self.main_start_game_menu.is_enabled():
            self.main_start_game_menu.mainloop(surface, self.bg_set())

    def change_player_number(self, value: Tuple[Any, int], player_number: int):
        self.player_number = player_number

    def get_player_number(self):
        return self.player_number

    def start_game(self):
        self.game_data_controller.load_from_new_game(self.get_player_number())
        self.main_start_game_menu.disable()

    def load_game(self, game_progress_data: GameProgressData):
        self.game_data_controller.load_from_game(game_progress_data)
        self.main_start_game_menu.disable()

    def bg_set(self):
        self.start_game_surface.fill(self.colour)
