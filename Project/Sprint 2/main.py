import pygame
import sys
import random
import math
from gameBoard import GameBoard

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    game_board = GameBoard(800, 600)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game_board.handle_input(event)

        game_board.update()
        game_board.play_turn()
        if game_board.game_over:
            running = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
