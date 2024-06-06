from abc import ABC, abstractmethod
from typing import List
from Player import Player
from LocationDataController import ILocationDataController
from Tile import Tile


class LocationManager:
    def __init__(self, location_data_controller: ILocationDataController):
        self._location_data_controller = location_data_controller

    def update_player_location(self, player: Player, tile: Tile) -> None:
        current_location = self.get_player_location(player)
        squares = self._location_data_controller.get_squares()
        for i in range(len(squares)):
            if current_location.is_cave() and squares[i].cave and squares[i].cave.get_occupant() and squares[i].cave.get_occupant().id == player.id:
                squares[i].cave.remove_occupant()
            if squares[i] == current_location:
                squares[i].remove_occupant()
            if squares[i] == tile:
                squares[i].set_occupant(player)
        self._location_data_controller.set_squares(squares)

    def set_player_location(self, player: Player, tile: Tile) -> None:
        squares = self._location_data_controller.get_squares()
        for i in range(len(squares)):
            if tile.is_cave() and squares[i].cave and squares[i].cave.id == tile.id:
                squares[i].cave.set_occupant(player)
            elif squares[i].id == tile.id:
                squares[i].set_occupant(player)
        self._location_data_controller.set_squares(squares)

    def remove_player_location(self, tile: Tile) -> None:
        squares = self._location_data_controller.get_squares()
        for i in range(len(squares)):
            if tile.is_cave() and squares[i].cave and squares[i].cave.id == tile.id:
                squares[i].cave.remove_occupant()
            elif squares[i].id == tile.id:
                squares[i].remove_occupant()
        self._location_data_controller.set_squares(squares)

    def get_closest_forward(self, tile_1: Tile, tile_2: Tile) -> List[Tile]:
        path = []
        current_tile = tile_1
        while current_tile is not None:
            if current_tile == tile_2:
                return path
            current_tile = current_tile.next
            path.append(current_tile)
        return []

    def get_closest_backward(self, tile_1: Tile, tile_2: Tile) -> List[Tile]:
        path = []
        current_tile = tile_1
        while current_tile is not None:
            if current_tile == tile_2:
                return path
            current_tile = current_tile.prev
            path.append(current_tile)
        return []

    def get_tiles_between(self, tile_1: Tile, tile_2: Tile) -> List[Tile]:
        """Get all tiles between two tiles. The output will be the shortest path between tile_1 and tile_2."""
        if tile_1 == tile_2:
            return [tile_1]

        # Get the forward and backward paths
        forward_path = self.get_closest_forward(tile_1, tile_2)
        backward_path = self.get_closest_backward(tile_1, tile_2)

        # Check which path is shorter
        if not forward_path and not backward_path:
            return []
        if not forward_path:
            return backward_path[::-1]
        if not backward_path:
            return forward_path

        return forward_path if len(forward_path) <= len(backward_path) else backward_path[::-1]


    def get_player_location(self, player) -> Tile:
        for square in self._location_data_controller.get_squares():
            if square.get_occupant() and square.get_occupant().id == player.id:
                return square
            if square.cave and square.cave.get_occupant() and square.cave.get_occupant().id == player.id:
                return square.cave


