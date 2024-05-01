
import pygame
from DragonCard import DragonCard
from Project.Sprint2.Square import Square
from VolcanoCard import VolcanoCard


class Volcano:
    def __init__(self, width, height, fps, num_volcano_card):
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption('Fiery Game')
        self.timer = pygame.time.Clock()
        self.fps = fps
        self.dragon_card = DragonCard()
        self.VolcanoCard = []
        for _ in range(num_volcano_card):
            self.VolcanoCard.append(VolcanoCard())



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
        square_size = radius // 2
        square_y = center_y - square_size // 2
        self.VolcanoCard[0].arrange_squares(70, square_y + 50,  center_x)
        self.VolcanoCard[0].draw(self.screen)
        self.VolcanoCard[1].arrange_squares(70,square_y + 600,  center_x)
        self.VolcanoCard[1].draw(self.screen)
        self.VolcanoCard[2].arrange_squares_diagonally(70,square_y-250,center_x+250)
        self.VolcanoCard[2].draw(self.screen)
        self.VolcanoCard[3].arrange_squares_vertically(70,square_y, center_x - 200)
        self.VolcanoCard[3].draw(self.screen)
        self.VolcanoCard[4].arrange_squares_vertically(70,square_y, center_x + 350)
        self.VolcanoCard[4].draw(self.screen)
        self.VolcanoCard[5].arrange_squares_diagonally(70,square_y+230,center_x -200)
        self.VolcanoCard[5].draw(self.screen)
        self.VolcanoCard[6].arrange_squares_diagonally_left(70,square_y - 250,center_x -150 )
        self.VolcanoCard[6].draw(self.screen)
        self.VolcanoCard[7].arrange_squares_diagonally_left(70,square_y + 250,center_x +350 )
        self.VolcanoCard[7].draw(self.screen)



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
    volcano_game = Volcano(1000, 800, 60,8)
    volcano_game.run()
