import time

import pygame

from Volcano import Volcano


class GameEngine:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 1200))

    def run(self):
        pygame.init()
        volcano = Volcano()
        running = True
        ####
        button_pos = (500, 600)
        button_size = (200, 100)

        # Create a Rect object for the button
        button_rect = pygame.Rect(button_pos, button_size)
        font = pygame.font.Font('freesansbold.ttf', 72)

        text = font.render('YOU WIN!!!!!!!!!!!!', True, (0, 0, 255), (255, 0, 0))

        # text surface object
        textRect = text.get_rect()
        textRect.center = (600, 600)
        ##########################
        check_win = False
        while running:
            self.screen.fill((255, 255, 255))
            volcano.render(self.screen)
            pygame.draw.rect(self.screen, (0, 0, 0), button_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(pygame.mouse.get_pos()):
                        self.screen.blit(text, textRect)
                        running = False


            pygame.display.flip()
            time.sleep(10)


if __name__ == '__main__':
    game = GameEngine()
    game.run()
