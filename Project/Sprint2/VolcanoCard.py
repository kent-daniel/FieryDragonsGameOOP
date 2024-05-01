from Square import Square


class VolcanoCard:
    def __init__(self):
        self.squares = None

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

