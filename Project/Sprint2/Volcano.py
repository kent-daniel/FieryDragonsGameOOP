import pygame
import sys

class VolcanoGame:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up display
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Fiery Dragon Game")

        # Load the image
        self.image_path = "Assets/VolcanoArena.png"  # Replace with the path to your image file
        self.image = pygame.image.load(self.image_path)

    def run_game(self):
        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the screen with black
            self.screen.fill((0, 0, 0))

            # Blit the image onto the screen
            self.screen.blit(self.image, (150, 50))  # Adjust the position as needed

            # Update the display
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()

# Create an instance of the game and run it
if __name__ == "__main__":
    game = VolcanoGame()
    game.run_game()
