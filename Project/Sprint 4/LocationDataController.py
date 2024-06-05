from abc import ABC, abstractmethod
from typing import List
from Square import Square


class ILocationDataController(ABC):
    """
    Author: Kent Daniel
    Interface for managing location data (squares ,cave , volcanoes ) in the game.
    """

    @abstractmethod
    def get_squares(self) -> List[Square]:
        pass

    @abstractmethod
    def set_squares(self, squares) -> None:
        pass

    @abstractmethod
    def get_num_volcanoes(self) -> int:
        pass

    @abstractmethod
    def to_json_format_square(self) -> List[dict]:
        pass


class LocationDataController(ILocationDataController):

    def __init__(self, squares: List[Square], num_volcanoes: int):
        self.num_volcanoes = num_volcanoes
        self.squares = self.create_tiles(squares)

    def get_squares(self) -> List[Square]:
        return self.squares

    def set_squares(self, squares: List[Square]) -> None:
        self.squares = squares

    def to_json_format_square(self) -> List[dict]:
        return [square.encode_to_json() for square in self.squares]

    def create_tiles(self, squares) -> List[Square]:
        square_tiles = []
        for square in squares:
            # link cave to square
            if square.cave:
                cave = square.cave
                cave.next = square
                cave.prev = None
                square.set_cave(cave)
            square_tiles.append(square)
        return self._link_tiles(square_tiles)

    def _link_tiles(self, square_tiles: List[Square]) -> List[Square]:
        for i in range(len(square_tiles)):
            square_tiles[i].next = square_tiles[(i + 1) % len(square_tiles)]
            square_tiles[i].prev = square_tiles[(i - 1) % len(square_tiles)]
        return square_tiles

    def get_num_volcanoes(self) -> int:
        return self.num_volcanoes
