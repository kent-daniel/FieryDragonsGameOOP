
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
        radius = min(self.WIDTH, self.HEIGHT) // 4
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
        self.arrange_volcano_cards(square_y,center_x)
        self.addPlayers()

    def arrange_volcano_cards(self, square_y, center_x):
        #top
        self.VolcanoCard[0].arrange_squares(60, square_y + 50 , center_x)
        self.VolcanoCard[0].draw(self.screen)
        #bottom
        self.VolcanoCard[1].arrange_squares(60,square_y + 600,  center_x + 10)
        self.VolcanoCard[1].draw(self.screen)
        #top right
        self.VolcanoCard[2].arrange_squares_diagonally(60,square_y-220,center_x+220)
        self.VolcanoCard[2].draw(self.screen)
        #left
        self.VolcanoCard[3].arrange_squares_vertically(60,square_y - 20, center_x - 200 )
        self.VolcanoCard[3].draw(self.screen)
        #right
        self.VolcanoCard[4].arrange_squares_vertically(60,square_y - 20, center_x + 330)
        self.VolcanoCard[4].draw(self.screen)
        #bottom left
        self.VolcanoCard[5].arrange_squares_diagonally(60,square_y+170,center_x -170)
        self.VolcanoCard[5].draw(self.screen)
        #top left
        self.VolcanoCard[6].arrange_squares_diagonally_left(60,square_y - 220,center_x - 100 )
        self.VolcanoCard[6].draw(self.screen)
        #bottom right
        self.VolcanoCard[7].arrange_squares_diagonally_left(60,square_y + 170,center_x +300 )
        self.VolcanoCard[7].draw(self.screen)



    def addPlayers(self):
        self.VolcanoCard[0].add_cave(self.screen, 0, -60)
        self.VolcanoCard[1].add_cave(self.screen,0,60)
        self.VolcanoCard[3].add_cave(self.screen,-60,0)
        self.VolcanoCard[4].add_cave(self.screen,60,0)






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
    volcano_game = Volcano(1000, 900, 60,8)
    volcano_game.run()
