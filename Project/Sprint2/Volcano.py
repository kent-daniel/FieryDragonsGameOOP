import sys

import pygame

from VolcanoCard import VolcanoCard
from Cave import Cave


class Volcano:
    def __init__(self):
        # pygame.init()
        # screen_size = (1000, 1000)
        # screen = pygame.display.set_mode(screen_size)
        # pygame.display.set_caption("")
        self.volc_color = (255, 0, 0)  # red
        self.background_color = (255, 255, 255)  # white

        # Set the position and radius of the circle
        self.volc_pos = (600, 600)
        self.volc_radius = 420
        self.volc_width = 69
        self.square_array = [[(496, 986), (600, 1000), (703, 986)], [(496, 204), (600, 200), (703, 204)],
                             [(214, 496), (200, 600), (214, 704)], [(986, 496), (1000, 600), (986, 704)],
                             [(946, 800), (883, 883), (800, 946)], [(254, 400), (317, 317), (400, 254)],
                             [(254, 800), (317, 883), (400, 946)],
                             [(946, 400), (883, 317), (800, 254)]]
        volcano_card1 = VolcanoCard()
        volcano_card2 = VolcanoCard()
        volcano_card3 = VolcanoCard()
        volcano_card4 = VolcanoCard()
        volcano_card5 = VolcanoCard()
        volcano_card6 = VolcanoCard()
        volcano_card7 = VolcanoCard()
        volcano_card8 = VolcanoCard()
        self.volcano_cards = [volcano_card1, volcano_card2, volcano_card3, volcano_card4, volcano_card5, volcano_card6,
                              volcano_card7, volcano_card8]
        self.cave_array = [(500, 20), (500, 1000), (20, 550), (1000, 550)]
        self.cave = Cave()

    def render(self, screen):
        screen.fill(self.background_color)

        # Draw the volcano
        pygame.draw.circle(screen, self.volc_color, self.volc_pos, self.volc_radius, width=self.volc_width)
        for k in self.cave_array:
            self.cave.render(screen, k)

        for i, j in zip(self.square_array, self.volcano_cards):
            j.render(screen, i)
    def win(self,screen,text,rect):
        screen.blit(text,rect)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1200, 1200))

    volcano = Volcano()
    running = True
    while running:
        screen.fill((255, 255, 255))
        volcano.render(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
