import pygame
from Character import CharacterImage
from Project.Sprint2.Player import Player


class Cave:
    def __init__(self):
        self.image = pygame.image.load(CharacterImage.PIRATE.value)
        self.player = Player(10)

    def display_cave(self, screen,cave_x, cave_y, square_size ):
        image = pygame.transform.scale(self.image, (square_size, square_size))
        screen.blit(image, (cave_x, cave_y))
        player_x = cave_x + (square_size // 2) - self.player.radius
        player_y = cave_y + (square_size // 2) - self.player.radius
        self.player.draw(screen, player_x, player_y)

