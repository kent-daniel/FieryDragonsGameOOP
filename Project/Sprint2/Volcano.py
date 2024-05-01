
import pygame
from DragonCard import DragonCard
from VolcanoCard import VolcanoCard


class Volcano:
    def __init__(self, num_volcano_card):
        self.dragon_card = DragonCard()
        self.VolcanoCard = []
        for _ in range(num_volcano_card):
            self.VolcanoCard.append(VolcanoCard())



    def set_volcano(self, width, height, screen):
        # Calculate the center of the screen
        center_x = width // 2
        center_y = height // 2
        # Draw circular board
        radius = min(width, height) // 4
        pygame.draw.circle(screen, 'brown', (center_x, center_y), radius)
        volcano_image = pygame.image.load("Assets/VolcanoArena.png")  # Load volcano image
        scaled_volcano_image = pygame.transform.scale(volcano_image, (radius * 2, radius * 2))
        # Calculate the position to blit the volcano image
        volcano_x = center_x - radius
        volcano_y = center_y - radius
        # Blit the volcano image onto the circular board
        screen.blit(scaled_volcano_image, (volcano_x, volcano_y))
        self.dragon_card.generate_random_cards(16)
        self.dragon_card.display_cards(center_x,center_y,radius, screen)
        square_size = radius // 2
        square_y = center_y - square_size // 2
        self.arrange_volcano_cards(square_y,center_x, screen)
        self.addPlayers(screen)

    def arrange_volcano_cards(self, square_y, center_x, screen):
        #top
        self.VolcanoCard[0].arrange_squares(60, square_y + 50 , center_x)
        self.VolcanoCard[0].draw(screen)
        #bottom
        self.VolcanoCard[1].arrange_squares(60,square_y + 600,  center_x + 10)
        self.VolcanoCard[1].draw(screen)
        #top right
        self.VolcanoCard[2].arrange_squares_diagonally(60,square_y-220,center_x+220)
        self.VolcanoCard[2].draw(screen)
        #left
        self.VolcanoCard[3].arrange_squares_vertically(60,square_y - 20, center_x - 200 )
        self.VolcanoCard[3].draw(screen)
        #right
        self.VolcanoCard[4].arrange_squares_vertically(60,square_y - 20, center_x + 330)
        self.VolcanoCard[4].draw(screen)
        #bottom left
        self.VolcanoCard[5].arrange_squares_diagonally(60,square_y+170,center_x -170)
        self.VolcanoCard[5].draw(screen)
        #top left
        self.VolcanoCard[6].arrange_squares_diagonally_left(60,square_y - 220,center_x - 100 )
        self.VolcanoCard[6].draw(screen)
        #bottom right
        self.VolcanoCard[7].arrange_squares_diagonally_left(60,square_y + 170,center_x +300 )
        self.VolcanoCard[7].draw(screen)



    def addPlayers(self, screen):
        self.VolcanoCard[0].squares[1].add_cave(screen, 0, -60)
        self.VolcanoCard[1].squares[1].add_cave(screen,0,60)
        self.VolcanoCard[3].squares[1].add_cave(screen,-60,0)
        self.VolcanoCard[4].squares[1].add_cave(screen,60,0)



