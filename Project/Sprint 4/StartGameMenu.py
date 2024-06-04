from typing import Tuple, Any
import pygame
from GameConstants import GameStyles
import pygame_menu


class StartGameMenu:
    def __init__(self, colour=GameStyles.COLOR_BROWN_DARK.value, games=[]):
        self.main_start_game_menu = None
        pygame.init()
        self.player_number = None
        self.colour = colour
        self.screen_width, self.screen_height = pygame.display.get_desktop_sizes()[0]
        self.start_game_surface: pygame.Surface = pygame.Surface((self.screen_width, self.screen_height),
                                                                 pygame.SRCALPHA)
        pygame.draw.rect(self.start_game_surface, colour, self.start_game_surface.get_rect(),
                         border_radius=GameStyles.BORDER_RADIUS_SMALL.value)
        self.games = games  #.get_previous_games()

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
                                        theme=self.menu_theme,
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
            self.previous_game_menu.add.button(pg, self.load_game)

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
        self.main_start_game_menu.disable()

    def load_game(self):
        pass

    def bg_set(self):
        self.start_game_surface.fill(GameStyles.COLOR_BROWN_LIGHT.value)


if __name__ == "__main__":
    pygame.init()
    screen_width, screen_height = pygame.display.get_desktop_sizes()[0]
    screen = pygame.display.set_mode((screen_width * 0.95, screen_height * 0.95), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    start_game_menu = StartGameMenu()
    start_game_menu.run_menu(screen)
