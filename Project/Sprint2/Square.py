import pygame
import Character


class Square:
    def __init__(self, img_link):
        self.img = pygame.image.load(img_link)
        pygame.transform.rotozoom(self.img, 0, 2)
        self.center = 0, 0
        self.rect = self.img.get_rect()

    def render(self, screen, position):
        self.rect.center = position
        screen.blit(self.img, self.rect)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    bat = Character.Character('bat')
    bat = bat.get_character()
    square = Square(bat)
    running = True
    while running:
        screen.fill((255, 255, 255))
        square.render(screen, (400, 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
