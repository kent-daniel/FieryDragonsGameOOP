from Square import Square


class Movement:
    def __init__(self, value: int, destination: Square):
        self._value = value
        self._destination = destination

    @property
    def value(self) -> int:
        return self._value

    @property
    def destination(self) -> Square:
        return self._destination
