from enum import Enum


class NotificationRecipientLevel(str, Enum):

    SESSION: str = 'session'
    USER: str = 'user'
    GROUP: str = 'group'
    ALL: str = 'all'

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)
