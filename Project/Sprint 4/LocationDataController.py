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
    def get_num_volcanoes(self) -> int:
        pass
    @abstractmethod
    def get_caves(self) -> List[Cave]:
        pass

    @abstractmethod
    def get_tiles(self) -> List[Tile]:
        pass
    @abstractmethod
    def set_tiles(self, tiles: List[Tile]) -> None:
        pass


class LocationDataController(ILocationDataController):

    def __init__(self, tiles_data: List[dict], caves_config_data: List[dict], players: deque[Player]):
        self._tiles_data = tiles_data
        self._caves_config_data = caves_config_data
        self.players = players
        self.tiles = self._create_tiles()

    def get_squares(self) -> List[Square]:
        return [tile for tile in self.tiles if isinstance(tile, Square)]

    def get_caves(self) -> List[Cave]:
        return [tile for tile in self.tiles if isinstance(tile, Cave)]

    def get_tiles(self) -> List[Tile]:
        return self.tiles

    def set_tiles(self, tiles: List[Tile]) -> None:
        self.tiles = tiles

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
                tiles[-1].attach_cave(cave_tile)
                tiles.append(cave_tile)

            else:
                square_tile = Square(index, animal)
                square_tile.set_occupant(occupant)
                tiles.append(square_tile)

        return self._link_tiles(tiles)

    def _link_tiles(self, tiles: List[Tile]) -> List[Tile]:
        for i in range(len(tiles)):
            tiles[i].next = tiles[(i + 1) % len(tiles)]
            tiles[i].prev = tiles[(i - 1) % len(tiles)]
        return tiles

    def get_num_volcanoes(self) -> int:
        return len(self.players) * 2
