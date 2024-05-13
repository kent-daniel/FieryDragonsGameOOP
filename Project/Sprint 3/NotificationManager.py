from collections import deque


class NotificationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._notifications = deque(maxlen=5)
        return cls._instance

    def add_notification(self, message: str):
        self._notifications.append(message)

    @property
    def notifications(self):
        return list(self._notifications)