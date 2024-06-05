from Tile import Tile
class Movement:
    def __init__(self,value:int , destination: Tile):
        self._value  = value
        self._destination = destination

    @property
    def value(self) -> int:
        return self._value

    @property
    def destination(self) -> Tile:
        return self._destination
