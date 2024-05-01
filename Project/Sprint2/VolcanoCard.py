import pygame
from Cave import Cave
from Square import Square


class VolcanoCard:
    def __init__(self):
        self.squares = None
        self.cave = Cave()

    def arrange_squares(self, square_size, square_y, center_x):
        square_x_offset = square_size // 2
        squares = [Square(center_x - square_x_offset - square_size, square_y- 300, square_size),
                   Square(center_x - square_x_offset - square_size + square_size, square_y- 300, square_size),
                   Square(center_x - square_x_offset - square_size + square_size * 2, square_y - 300, square_size)]
        self.squares = squares
        return squares

    def arrange_squares_diagonally(self, square_size, square_y, center_x):
        # Calculate positions for the three squares
        square1_x = center_x - square_size // 2 - square_size
        square1_y = square_y

        square2_x = center_x - square_size // 2 - 10
        square2_y = square_y + square_size

        square3_x = center_x - square_size // 2 + square_size -20
        square3_y = square_y + square_size * 2

        # Create instances of Square with calculated positions
        square1 = Square(square1_x, square1_y, square_size)
        square2 = Square(square2_x, square2_y, square_size)
        square3 = Square(square3_x, square3_y, square_size)

        # Return the list of squares
        self.squares = [square1, square2, square3]
        return self.squares

    def arrange_squares_vertically(self, square_size, square_y, center_x):
        # Calculate positions for the three squares
        square1_x = center_x - square_size // 2 - square_size
        square1_y = square_y

        square2_x = center_x - square_size // 2 - square_size
        square2_y = square_y + square_size

        square3_x = center_x - square_size // 2 + square_size - square_size - square_size
        square3_y = square_y + square_size * 2

        # Create instances of Square with calculated positions
        square1 = Square(square1_x, square1_y, square_size)
        square2 = Square(square2_x, square2_y, square_size)
        square3 = Square(square3_x, square3_y, square_size)

        # Return the list of squares
        self.squares = [square1, square2, square3]
        return self.squares

    def arrange_squares_diagonally_left(self, square_size, square_y, center_x):
        # Calculate positions for the three squares
        square1_x = center_x - square_size // 2 - square_size
        square1_y = square_y

        square2_x = center_x - square_size // 2 - square_size - square_size + 20
        square2_y = square_y + square_size

        square3_x = center_x - square_size // 2 + square_size - square_size * 4 + 40
        square3_y = square_y + square_size * 2

        # Create instances of Square with calculated positions
        square1 = Square(square1_x, square1_y, square_size)
        square2 = Square(square2_x, square2_y, square_size)
        square3 = Square(square3_x, square3_y, square_size)

        # Return the list of squares
        self.squares = [square1, square2, square3]
        return self.squares

    def draw(self, screen):
        for square in self.squares:
            square.draw(screen)

    def add_cave(self, screen, x, y):
        if len(self.squares) >= 2:  # Check if there are at least two squares in the list
            # Load the cave image
            cave_image = self.cave.image
            # Resize the cave image to fit the size of the square
            cave_image = pygame.transform.scale(cave_image, (self.squares[1].size, self.squares[1].size))
            # Set the image of the second square to the cave image
            self.squares[1].image = cave_image
            # Calculate the position to blit the cave image (same as the position of the second square)
            cave_x = self.squares[1].x + x
            cave_y = self.squares[1].y + y
            # Blit the cave image onto the screen
            screen.blit(cave_image, (cave_x, cave_y))

