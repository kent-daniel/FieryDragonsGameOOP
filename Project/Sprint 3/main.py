import GameConstants
from Game import Game
import pygame
from GameDataController import GameDataController


def main():
    pygame.init()
    screen_width, screen_height = pygame.display.get_desktop_sizes()[0]
    screen = pygame.display.set_mode((screen_width * 0.95, screen_height * 0.95), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Fiery Dragons")
    game_data_controller = GameDataController("config.ini")
    game = Game(game_data_controller, screen)
    FPS = 60

    while game.is_running:
        game.handle_events()
        screen.fill(GameConstants.GameStyles.COLOR_GRAY_700.value)
        game.render_game()
        pygame.display.flip()
        clock.tick(FPS)  # Frame rate


if __name__ == '__main__':
    main()
