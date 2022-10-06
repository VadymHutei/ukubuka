from enum import Enum


class NotificationType(str, Enum):

    INFO_TYPE: str = 'info'
    WARNING_TYPE: str = 'warning'
    SUCCESS_TYPE: str = 'success'
    ERROR_TYPE: str = 'error'

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)
