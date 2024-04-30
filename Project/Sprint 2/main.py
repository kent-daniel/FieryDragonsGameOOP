import pygame
import sys

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Circular Board Example")

# Colors
WHITE = (255, 255, 255)

# Create a circular surface
circle_radius = 200
circle_surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(circle_surface, WHITE, (circle_radius, circle_radius), circle_radius)

# Load an image
image = pygame.image.load("assets/VolcanoArena.png").convert_alpha()
image = pygame.transform.scale(image, (circle_radius * 2, circle_radius * 2))

# Blit the image onto the circular surface
circle_surface.blit(image, (0, 0))

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
