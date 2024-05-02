import pygame
import random
from Square import Square
from Character import Character

class VolcanoCard:
    def __init__(self):
        self.squares = []
        self.generate_squares()
        # self.character = Character()

    def generate_squares(self):
        for _ in range(3):
            random_character = random.choice(['bat', 'dragon', 'spider', 'salamander'])
            character_img_link = Character(random_character)
            square = Square(character_img_link.get_character())
            self.squares.append(square)

    def render(self, screen, positions):
        for square, position in zip(self.squares, positions):
            square.render(screen, position)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    volcano_card = VolcanoCard()
    running = True
    while running:
        screen.fill((255, 255, 255))
        volcano_card.render(screen, [(300, 200), (400, 200), (500, 200)])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
