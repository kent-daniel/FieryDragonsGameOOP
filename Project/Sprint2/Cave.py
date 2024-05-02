import pygame


class Cave:
    def __init__(self):
        self.cave = pygame.image.load("Assets/Cave.png")
        DEFAULT_CAVE_SIZE = (200, 200)
        self.cave = pygame.transform.scale(self.cave, DEFAULT_CAVE_SIZE)

    def render(self, screen, position):
        screen.blit(self.cave, position)
