import pygame
import sys
import random

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fiery Dragons")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a circular surface
circle_radius = 200
circle_surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(circle_surface, WHITE, (circle_radius, circle_radius), circle_radius)

# Load an image
image = pygame.image.load("assets/VolcanoArena.png").convert_alpha()
image = pygame.transform.scale(image, (circle_radius * 2, circle_radius * 2))

# Blit the image onto the circular surface
circle_surface.blit(image, (0, 0))

# Load the images
images = [
    pygame.image.load("assets/BabySpider.png").convert_alpha(),
    pygame.image.load("assets/BabyDragon.png").convert_alpha(),
    pygame.image.load("assets/BabyBat.png").convert_alpha(),
    pygame.image.load("assets/Salamander.png").convert_alpha()
]
image_size = circle_radius // 4  # Size of each image in the grid

# Create a grid of random images
grid = [[random.choice(images) for _ in range(4)] for _ in range(4)]
# Create a grid to track the visibility state of each image
flipped_grid = [[False for _ in range(4)] for _ in range(4)]

# Calculate the starting position of the grid to center it in the circle
start_x = circle_radius - (image_size * 2)
start_y = circle_radius - (image_size * 2)

# Blit the grid onto the circular surface
for i in range(4):
    for j in range(4):
        image = pygame.transform.scale(grid[i][j], (image_size, image_size))
        circle_surface.blit(image, (start_x + j * image_size, start_y + i * image_size))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Blit the circular surface onto the screen
    screen.blit(circle_surface, (width // 2 - circle_radius, height // 2 - circle_radius))

    pygame.display.flip()

pygame.quit()
sys.exit()
