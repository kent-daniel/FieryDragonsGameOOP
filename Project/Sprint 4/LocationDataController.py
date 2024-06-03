from abc import ABC, abstractmethod
from collections import deque
from typing import List
from Cave import Cave
from Square import Square
from GameConstants import CharacterImage
from Player import Player
from Tile import Tile

class ILocationDataController(ABC):
    """
    Author: Kent Daniel
    Interface for managing location data (squares ,cave , volcanoes ) in the game.
    """

    @abstractmethod
    def get_squares(self) -> List[Square]:
        pass

    @abstractmethod
    def set_squares(self, squares: List[Square]) -> None:
        pass

    @abstractmethod
    def get_num_volcanoes(self) -> int:
        pass
    @abstractmethod
    def get_caves(self) -> List[Cave]:
        pass

    @abstractmethod
    def set_caves(self, caves: List[Cave]) -> None:
        pass


class LocationDataController(ILocationDataController):

    def __init__(self, tiles_data: List[dict], caves_config_data: List[dict], players: deque[Player]):
        self._tiles_data = tiles_data
        self._caves_config_data = caves_config_data
        self.players = players
        self.squares = []
        self.caves = []
        self.tiles = self._create_tiles()

    def get_squares(self) -> List[Square]:
        return self.squares

    def set_squares(self, squares: List[Square]) -> None:
        pass

    def _create_tiles(self) -> List[Tile]:
        tiles = []
        for index, tile_data in enumerate(self._tiles_data):
            cave = next((cave for cave in self._caves_config_data if cave["position"] == index), None)
            occupant = next((player for player in self.players if tile_data["occupant"] == player.id), None)
            animal = CharacterImage[tile_data["animal"]]

            # Check if the current tile is a cave
            if cave:
                owner = next((player for player in self.players if cave["owner"] == player.id), None)
                cave_tile = Cave(index, owner, animal)
                cave_tile.set_occupant(occupant)

                # attach cave to previous tile
                self.squares[-1].attach_cave(cave_tile)
                tiles.append(cave_tile)
                self.caves.append(cave_tile)
            else:
                square_tile = Square(index, animal)
                square_tile.set_occupant(occupant)
                tiles.append(square_tile)
                self.squares.append(square_tile)

        return self._link_tiles(tiles)

    def _link_tiles(self, tiles: List[Tile]) -> List[Tile]:
        for i in range(len(tiles)):
            tiles[i].next = tiles[(i + 1) % len(tiles)]
            tiles[i].prev = tiles[(i - 1) % len(tiles)]
        return tiles

    def get_caves(self) -> List[Cave]:
        pass

    def set_caves(self, caves: List[Cave]) -> None:
        pass

    def get_num_volcanoes(self) -> int:
        print(len(self.players) , len(self.squares) , len(self.tiles))
        return len(self.players) * 2

    # def _create_tiles(self) -> None:
    #     squares_list = self._parse_squares()
    #     player_index = 0
    #     num_volcanoes = len(self._players) * 2
    #     volcano_size = len(squares_list) // num_volcanoes
    #     for i in range(num_volcanoes):
    #         start_index = i * volcano_size
    #         end_index = start_index + volcano_size
    #         card_squares = squares_list[start_index:end_index]
    #         if i % 2 == 0:
    #             central_square_index = len(card_squares) // 2
    #             card_squares[central_square_index].attach_cave(Cave(self._players[player_index]))
    #             card_squares[central_square_index].set_occupant(self._players[player_index])
    #             player_index += 1
    #         self._squares += card_squares
