from collections import deque


class NotificationManager:
    """
    Notification Manager

    Authored by: Kent Daniel

    This class defines a singleton NotificationManager that manages a list
    of notifications. It ensures only the most recent notifications are kept,
    up to a maximum limit.

    Methods:
        add_notification(message: str) -> None:
            Adds a new notification to the list.
        notifications() -> list:
            Returns the current list of notifications.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._notifications = deque(maxlen=5)
        return cls._instance

    def add_notification(self, message: str, level: str = "info"):
        self._notifications.append({"message": message, "level": level})

    @property
    def notifications(self):
        return list(self._notifications)
