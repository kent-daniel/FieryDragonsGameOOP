import pygame
import sys
import random
import math

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Cave:
    def __init__(self, color):
        self.color = color

class Dragon:
    def __init__(self, color):
        self.color = color
        self.position = None

class DragonCard:
    def __init__(self, animals):
        self.animals = animals
        self.is_pirate = any(animal == "Pirate" for animal in animals)

class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fiery Dragons")

        # Create a circular surface
        self.circle_radius = 200
        self.circle_surface = pygame.Surface((self.circle_radius * 2, self.circle_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.circle_surface, WHITE, (self.circle_radius, self.circle_radius), self.circle_radius)

        # Load the arena image
        self.arena_image = pygame.image.load("assets/VolcanoArena.png").convert_alpha()
        self.arena_image = pygame.transform.scale(self.arena_image, (self.circle_radius * 2, self.circle_radius * 2))
        self.circle_surface.blit(self.arena_image, (0, 0))

        # Load the animal images
        self.images = [
            pygame.image.load("assets/BabySpider.png").convert_alpha(),
            pygame.image.load("assets/BabyDragon.png").convert_alpha(),
            pygame.image.load("assets/BabyBat.png").convert_alpha(),
            pygame.image.load("assets/Salamander.png").convert_alpha()
        ]
        self.image_size = self.circle_radius // 4  # Size of each image in the grid

        # Create a grid of random images
        self.grid_images = [[random.choice(self.images) for _ in range(4)] for _ in range(4)]
        self.revealed_grid = [[False for _ in range(4)] for _ in range(4)]

        # Calculate the starting position of the grid to center it in the circle
        self.start_x = self.circle_radius - (self.image_size * 2)
        self.start_y = self.circle_radius - (self.image_size * 2)

        # Create the volcano cards
        self.volcano_cards = []
        self.create_volcano_cards()

        # Create the dragons and caves
        self.cave_colors = ["Red", "Blue", "Green", "Yellow"]
        self.caves = [Cave(color) for color in self.cave_colors]
        self.dragon_colors = self.cave_colors
        self.dragons = [Dragon(color) for color in self.dragon_colors]
        self.place_dragons_and_caves()

        self.dragon_cards = self.create_dragon_cards()
        random.shuffle(self.dragon_cards)

        self.flipped_card = None
        self.current_player = 0
        self.game_over = False

    def place_dragons_and_caves(self):
        for volcano_card, card_position in self.volcano_cards:
            if card_position.collidepoint(self.width // 2, self.height // 2):
                cave = self.caves.pop(0)
                dragon = self.dragons.pop(0)
                dragon.position = cave

    def create_volcano_cards(self):
        num_cards = 8
        angle_step = 360 / num_cards
        card_width = 60
        card_height = 60 * 3
        offset = 35

        for i in range(num_cards):
            angle = i * angle_step
            card_center = self.point_on_circle((self.width // 2, self.height // 2), self.circle_radius + offset, angle)
            card_surface = pygame.Surface((card_width, card_height), pygame.SRCALPHA)
            card_surface.fill((255, 255, 255, 0))

            padding = 5
            square_size = card_height // 3
            for j in range(3):
                square_image = random.choice(self.images)
                scaled_image = pygame.transform.scale(square_image, (square_size, square_size))
                square_surface = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
                square_surface.blit(scaled_image, (0, 0))
                card_surface.blit(square_surface, (0, j * square_size))

            card_surface = pygame.transform.rotate(card_surface, -angle)
            card_position = card_surface.get_rect(center=card_center)
            self.volcano_cards.append((card_surface, card_position))

    def create_dragon_cards(self):
        return [
            DragonCard(animals=["Salamander", "Salamander", "Salamander"]),
            DragonCard(animals=["Spider", "Spider"]),
            DragonCard(animals=["Baby Dragon"]),
            DragonCard(animals=["Bat"]),
            DragonCard(animals=["Salamander", "Bat"]),
            DragonCard(animals=["Spider", "Pirate"]),
            DragonCard(animals=["Baby Dragon", "Pirate"]),
            DragonCard(animals=["Salamander", "Salamander", "Bat"]),
            DragonCard(animals=["Spider", "Spider", "Pirate"]),
            DragonCard(animals=["Baby Dragon", "Baby Dragon", "Pirate"]),
            DragonCard(animals=["Salamander", "Bat", "Bat"]),
            DragonCard(animals=["Spider", "Spider", "Spider"]),
            DragonCard(animals=["Baby Dragon", "Baby Dragon", "Baby Dragon"]),
            DragonCard(animals=["Bat", "Bat", "Bat"]),
            DragonCard(animals=["Salamander", "Salamander", "Spider"]),
            DragonCard(animals=["Pirate", "Pirate"])
        ]

    def point_on_circle(self, center, radius, angle_deg):
        angle_rad = math.radians(angle_deg)
        x = center[0] + radius * math.cos(angle_rad)
        y = center[1] + radius * math.sin(angle_rad)
        return int(x), int(y)

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_x = (mouse_x - (self.width // 2 - self.circle_radius) - self.start_x) // self.image_size
            grid_y = (mouse_y - (self.height // 2 - self.circle_radius) - self.start_y) // self.image_size
            if 0 <= grid_x < 4 and 0 <= grid_y < 4:
                if self.flipped_card is None:
                    self.flipped_card = (grid_x, grid_y)
                elif self.flipped_card == (grid_x, grid_y):
                    self.flipped_card = None
                else:
                    self.flipped_card = (grid_x, grid_y)

    def update(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.circle_surface, (self.width // 2 - self.circle_radius, self.height // 2 - self.circle_radius))

        for i in range(4):
            for j in range(4):
                image_x = self.start_x + j * self.image_size
                image_y = self.start_y + i * self.image_size
                if (j, i) == self.flipped_card:
                    image = pygame.transform.scale(self.grid_images[i][j], (self.image_size, self.image_size))
                    self.circle_surface.blit(image, (image_x, image_y))
                else:
                    rect = (image_x, image_y, self.image_size, self.image_size)
                    pygame.draw.rect(self.circle_surface, (255, 255, 255, 100), rect, 0)

        for card_surface, card_position in self.volcano_cards:
            self.screen.blit(card_surface, card_position)

        pygame.display.flip()

    def play_turn(self):
        dragon = self.dragons[self.current_player]
        print(f"Player {self.current_player + 1}'s turn. {dragon.color} dragon is at position {dragon.position.color if dragon.position else 'None'}")

        # Draw a dragon card
        if not self.dragon_cards:
            self.dragon_cards = self.create_dragon_cards()
            random.shuffle(self.dragon_cards)
        dragon_card = self.dragon_cards.pop(0)
        print(f"Drawn card: {', '.join(dragon_card.animals)}")

        # Move the dragon
        if dragon.position is None:
            print("Dragon is still in its cave, no movement.")
        else:
            if any(animal == dragon.position.color for animal in dragon_card.animals):
                # Move the dragon forward
                num_moves = len([animal for animal in dragon_card.animals if animal != "Pirate"])
                print(f"Moving {dragon.color} dragon forward {num_moves} spaces.")
            elif dragon_card.is_pirate:
                # Move the dragon backward
                num_moves = len([animal for animal in dragon_card.animals if animal == "Pirate"])
                print(f"Moving {dragon.color} dragon backward {num_moves} spaces.")
            else:
                print(f"No match found, {dragon.color} dragon stays put.")

        self.current_player = (self.current_player + 1) % len(self.dragons)

        # Check if the game is over
        if any(dragon.position == cave for dragon in self.dragons for cave in self.caves):
            self.game_over = True
            print("Game over! A player has won.")

def main():
    game_board = GameBoard(800, 600)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game_board.handle_input(event)

        game_board.update()
        game_board.play_turn()
        if game_board.game_over:
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()