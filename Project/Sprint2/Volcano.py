
import pygame
from DragonCard import DragonCard
from Project.Sprint2.Square import Square
from VolcanoCard import VolcanoCard


class Volcano:
    def __init__(self, width, height, fps):
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption('Fiery Game')
        self.timer = pygame.time.Clock()
        self.fps = fps
        self.dragon_card = DragonCard()
        self.VolcanoCard = VolcanoCard()

    def set_volcano(self):
        # Calculate the center of the screen
        center_x = self.WIDTH // 2
        center_y = self.HEIGHT // 2
        # Draw circular board
        radius = min(self.WIDTH, self.HEIGHT) // 3
        pygame.draw.circle(self.screen, 'brown', (center_x, center_y), radius)
        volcano_image = pygame.image.load("Assets/VolcanoArena.png")  # Load volcano image
        scaled_volcano_image = pygame.transform.scale(volcano_image, (radius * 2, radius * 2))
        # Calculate the position to blit the volcano image
        volcano_x = center_x - radius
        volcano_y = center_y - radius
        # Blit the volcano image onto the circular board
        self.screen.blit(scaled_volcano_image, (volcano_x, volcano_y))
        self.dragon_card.generate_random_cards(16)
        self.dragon_card.display_cards(center_x,center_y,radius, self.screen)


        # Generate 3 squares
        square_size = radius // 2
        square_y = center_y - square_size // 2
        square_x_offset = square_size // 2
        squares = [Square(center_x - square_x_offset - square_size, square_y- 300, square_size),
                   Square(center_x - square_x_offset - square_size + radius // 2, square_y- 300, square_size),
                   Square(center_x - square_x_offset - square_size + radius, square_y - 300, square_size)]

        # Draw squares
        for square in squares:
            square.draw(self.screen)

    def run(self):
        running = True
        self.set_volcano()  # Draw the volcano and cards once before the game loop starts
        while running:
            self.timer.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()

        pygame.quit()

    # Example usage:
if __name__ == "__main__":
    volcano_game = Volcano(1000, 800, 60)
    volcano_game.run()
