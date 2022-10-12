from dataclasses import dataclass

from modules.Notification.entities.NotificationType import NotificationType


@dataclass
class Notification:

    text: str
    type: NotificationType = NotificationType.INFO_TYPE
