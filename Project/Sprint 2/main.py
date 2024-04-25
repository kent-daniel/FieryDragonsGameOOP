from Square import Square
import GameConstants
from Game import Game
from DragonCardsGroup import DragonCardsGroup
import pygame
from GameDataController import GameDataController
from Board import Board

def main():
    pygame.init()
    screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0], pygame.RESIZABLE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Fiery Dragons")
    config_path = "config.ini"

    game = Game(config_path, screen)


    running: bool = True
    while running:

        game.handle_events()
        ## scan events
        # for event in pygame.event.get():
        #     mouse_x, mouse_y = pygame.mouse.get_pos()
        #     if event.type == pygame.QUIT:
        #         running = False
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         pass
                # update cards
                #
                # for card in dragon_cards:
                #     if card.isClicked((mouse_x, mouse_y)):
                #         print(card)
                #         # cardResult = card.action(playerSquare)

                # volcano_card = VolcanoCard([square, square, square])
                # rotation += 360 // 8
                # volcano_card.rotate(rotation, (screen.get_width() // 2, screen.get_height() // 2))
                # volcanos.append(volcano_card)

        # Drawing the cards
        screen.fill(GameConstants.GameStyles.COLOR_GRAY_700.value)  # Clear screen with white color
        # for card in dragon_cards:
        #     card.render(screen)
        game.render_game()
        # for volcano in volcanos:
        #     volcano.draw(screen)

        # print(psutil.virtual_memory().percent)

        pygame.display.flip()
        clock.tick(60)  # Frame rate


def read_game_config():
    pass





if __name__ == '__main__':
    main()
