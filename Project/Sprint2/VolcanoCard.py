from Square import Square


class VolcanoCard:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.squares = self.generate_squares()

    def generate_squares(self, ):
        square_size = self.size // 3
        squares = []
        for i in range(3):
            squares.append(Square(self.x + i * square_size, self.y, square_size))
        return squares

    def draw(self, screen):
        for square in self.squares:
            square.draw(screen)