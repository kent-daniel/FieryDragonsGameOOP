import pygame

from Project.Sprint2.HandleClick import HandleClick
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
        self.click_handler = HandleClick(self.volcano)

    def process_turn(self, clicked_card):
        font = pygame.font.Font(None, 36)
        text = font.render(f"{clicked_card}'s Turn", True, (0, 0, 0))  # Render text with black color
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.fill((0, 0, 0), text_rect)  # Fill the text area with black
        # Render and blit the new text
        text = font.render(f"{clicked_card}'s Turn", True, (255, 255, 255))
        self.screen.blit(text, text_rect)


    def add_player(self, screen):
        self.volcano.VolcanoCard[0].squares[1].add_cave(screen, 0, -60, "Player1")
        self.volcano.VolcanoCard[1].squares[1].add_cave(screen,0,60, "Player3")
        self.volcano.VolcanoCard[3].squares[1].add_cave(screen,-60,0, "Player4")
        self.volcano.VolcanoCard[4].squares[1].add_cave(screen,60,0, "Player2")


    def start_game(self):
        pygame.init()
        running = True
        self.volcano.set_volcano(self.width, self.height, self.screen)
        self.add_player(self.screen)
        while running:
            self.timer.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button click
                        x, y = pygame.mouse.get_pos()
                        clicked_card = self.click_handler.handle_click(x, y)
                        if clicked_card:
                            self.process_turn(clicked_card)
            pygame.display.flip()

        pygame.quit()



if __name__ == "__main__":
    game_manager = GameManager(1000, 900, 60, 8)
    game_manager.start_game()