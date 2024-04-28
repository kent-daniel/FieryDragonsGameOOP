import logging
from abc import ABC, abstractmethod
from Movement import Movement


class IMovementEventListener(ABC):
    @abstractmethod
    def on_movement_event(self, movement: Movement) -> None:
        pass


class IMovementEventManager(ABC):
    @abstractmethod
    def add_listener(self, listener: IMovementEventListener) -> None:
        pass

    @abstractmethod
    def remove_event_listener(self, listener: IMovementEventListener) -> None:
        pass

    @abstractmethod
    def publish_event(self, movement: Movement) -> None:
        pass


class MovementEventManager(IMovementEventManager):
    def __init__(self):
        self._listeners = []

    def add_listener(self, listener: IMovementEventListener) -> None:
        self._listeners.append(listener)

    def remove_event_listener(self, listener: IMovementEventListener) -> None:
        self._listeners.remove(listener)

    def publish_event(self, movement: Movement) -> None:
        logging.log(1,"publish movement", movement.value, movement.destination.character)
        for listener in self._listeners:
            listener.on_movement_event(movement)
