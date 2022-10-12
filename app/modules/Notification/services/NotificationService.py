from datetime import timedelta
from typing import Optional

from modules.Notification.entities.NotificationEntity import Notification
from modules.Notification.entities.NotificationRecipient import NotificationRecipient
from modules.Notification.repositories.NotificationRedisRepository import NotificationRedisRepository


class NotificationService:

    def __init__(self):
        self._repository = NotificationRedisRepository()

    def push_notification(
        self,
        notification: Notification,
        recipient: NotificationRecipient,
        endpoint: Optional[str] = None,
        key_data: Optional[dict[str, str]] = None,
        TTL: Optional[timedelta] = None,
    ):
        self._repository.push_notification(notification, recipient, endpoint, key_data, TTL)

    def pop_notifications(
        self,
        recipient: NotificationRecipient,
        endpoint: Optional[str] = None,
        key_data: Optional[dict[str, str]] = None,
        by_pattern: bool = False,
    ) -> list[Notification]:
        return self._repository.pop_notifications(recipient, endpoint, key_data, by_pattern)
