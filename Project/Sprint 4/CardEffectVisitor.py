from abc import ABC, abstractmethod
from Square import Square
from Movement import Movement
from GameConstants import CharacterImage

class CardEffectVisitor(ABC):
    @abstractmethod
    def visit(self, square: Square) -> Movement:
        pass


class AnimalDragonCardEffectVisitor(CardEffectVisitor):
    def __init__(self, value: int):
        self.value = value

    def visit(self, square: Square) -> Movement:
        if square.character != CharacterImage.BABY_DRAGON:
            return Movement(0, square)
        destination = square
        for i in range(self.value):
            destination = destination.next

        return Movement(self.value, destination)

class PirateDragonCardEffectVisitor(CardEffectVisitor):
    def __init__(self, value: int):
        self.value = value

    def visit(self, square: Square) -> Movement:
        destination = square
        for i in range(self.value):
            destination = destination.prev
        return Movement(-self.value, destination)