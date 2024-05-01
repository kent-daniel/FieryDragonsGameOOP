import pygame

from Project.Sprint2.Volcano import Volcano


class GameManager:
    def __init__(self, width, height, fps, num_volcano_card):
        self.width = width
        self.height = height
        pygame.display.set_caption('Fiery Game')
        self.fps = fps
        self.num_volcano_card = num_volcano_card
        self.volcano = Volcano(8)
        self.timer = pygame.time.Clock()
        self.screen = pygame.display.set_mode([self.width, self.height])

    def start_game(self):
        pygame.init()
        running = True
        self.volcano.set_volcano(self.width, self.height, self.screen)
        while running:
            self.timer.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game_manager = GameManager(1000, 900, 60, 8)
    game_manager.start_game()