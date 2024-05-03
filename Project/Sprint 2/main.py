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
grid_images = [[random.choice(images) for _ in range(4)] for _ in range(4)]
# Create a grid to track whether each image is flipped or not
revealed_grid = [[False for _ in range(4)] for _ in range(4)]

# Calculate the starting position of the grid to center it in the circle
start_x = circle_radius - (image_size * 2)
start_y = circle_radius - (image_size * 2)


# Function to check if a point is inside a rectangle
def point_in_rect(point, rect):
    x, y = point
    rx, ry, rw, rh = rect
    return rx <= x <= rx + rw and ry <= y <= ry + rh

# Main loop
running = True
flipped_card = None  # Track the currently flipped card
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            # Check if a grid box was clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_x = (mouse_x - (width // 2 - circle_radius) - start_x) // image_size
            grid_y = (mouse_y - (height // 2 - circle_radius) - start_y) // image_size
            if 0 <= grid_x < 4 and 0 <= grid_y < 4:
                if flipped_card is None:
                    flipped_card = (grid_x, grid_y)
                elif flipped_card == (grid_x, grid_y):
                    flipped_card = None
                else:
                    flipped_card = (grid_x, grid_y)

    # Clear the screen
    screen.fill(BLACK)

    # Blit the circular surface onto the screen
    screen.blit(circle_surface, (width // 2 - circle_radius, height // 2 - circle_radius))

    # Blit the images onto the circular surface based on the revealed state
    for i in range(4):
        for j in range(4):
            image_x = start_x + j * image_size
            image_y = start_y + i * image_size
            if (j, i) == flipped_card:
                image = pygame.transform.scale(grid_images[i][j], (image_size, image_size))
                circle_surface.blit(image, (image_x, image_y))
            else:
                rect = (start_x + j * image_size, start_y + i * image_size, image_size, image_size)
                pygame.draw.rect(circle_surface, (255, 255, 255, 100), rect, 0)  # Draw a white rectangle for the cell

    pygame.display.flip()

pygame.quit()
sys.exit()
