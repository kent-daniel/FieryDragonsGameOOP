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

    def get_tiles_between(self, tile_1: Tile, tile_2: Tile) -> List[Tile]:
        """Get all tiles between two tiles, the output will be the shortest tiles path to between tile_1 and tile_2"""
        if tile_1 == tile_2:
            return [tile_1]

        forward_tiles_1 = []
        forward_tiles_2 = []

        current_tile_1 = tile_1
        current_tile_2 = tile_2

        # Simultaneous traversal from both tiles
        while True:
            if current_tile_1 is not None:
                forward_tiles_1.append(current_tile_1)
                if current_tile_1 == tile_2:
                    return forward_tiles_1
                current_tile_1 = current_tile_1.next

            if current_tile_2 is not None:
                forward_tiles_2.append(current_tile_2)
                if current_tile_2 == tile_1:
                    return forward_tiles_2[::-1]
                current_tile_2 = current_tile_2.next

            # If we reach the end in either direction without finding the target tile
            if current_tile_1 is None and current_tile_2 is None:
                break

    def get_player_location(self, player) -> Tile:
        for square in self._location_data_controller.get_squares():
            if square.get_occupant() and square.get_occupant().id == player.id:
                return square
            if square.cave and square.cave.get_occupant() and square.cave.get_occupant().id == player.id:
                return square.cave


