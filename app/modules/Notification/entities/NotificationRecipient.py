from enum import Enum


class NotificationRecipient(str, Enum):

    USER: str = 'user'
    ALL: str = 'all'

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)
