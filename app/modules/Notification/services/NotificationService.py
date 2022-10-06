from datetime import timedelta
from typing import Optional

from modules.Notification.entities.NotificationEntity import NotificationEntity
from modules.Notification.repositories.NotificationRedisRepository import NotificationRedisRepository


class NotificationService:

    @staticmethod
    def add_notification(
        notification: NotificationEntity,
        endpoint: Optional[str] = None,
        form: Optional[str] = None,
        TTL: Optional[timedelta] = None,
    ):
        repository = NotificationRedisRepository()
        repository.add_notification(notification, endpoint, form, TTL)
