from datetime import timedelta
from typing import Optional

from modules.Notification.entities.NotificationEntity import NotificationEntity
from modules.Notification.entities.NotificationRecipient import NotificationRecipient
from modules.Notification.repositories.NotificationRedisRepository import NotificationRedisRepository


class NotificationService:

    @staticmethod
    def add_notification(
        notification: NotificationEntity,
        endpoint: Optional[str] = None,
        form: Optional[str] = None,
        recipient: NotificationRecipient = NotificationRecipient.USER,
        TTL: Optional[timedelta] = None,
    ):
        repository = NotificationRedisRepository()
        repository.add_notification(notification, endpoint, form, recipient, TTL)

    @staticmethod
    def get_notifications(
        endpoint: Optional[str] = None,
        form: Optional[str] = None
    ) -> list[NotificationEntity]:
        repository = NotificationRedisRepository()
        return repository.get_notifications(endpoint, form)
