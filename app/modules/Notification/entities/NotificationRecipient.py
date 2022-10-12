from dataclasses import dataclass

from modules.Notification.entities.NotificationRecipientLevel import NotificationRecipientLevel


@dataclass
class NotificationRecipient:

    level: NotificationRecipientLevel
    value: str
