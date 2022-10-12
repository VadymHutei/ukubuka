from datetime import datetime, timedelta
from typing import Optional

from flask import g
from modules.Notification.entities.NotificationEntity import Notification
from modules.Notification.entities.NotificationRecipient import NotificationRecipient
from modules.Notification.entities.NotificationRecipientLevel import NotificationRecipientLevel
from modules.Notification.repositories.NotificationRedisRepository import NotificationRedisRepository


class NotificationService:

    def __init__(self):
        self._repository = NotificationRedisRepository()

    def set_notification(
        self,
        notification: Notification,
        recipient: NotificationRecipient,
        endpoint: Optional[str] = None,
        key_data: Optional[dict[str, str]] = None,
        TTL: Optional[timedelta] = None,
    ):
        self._repository.set_notification(notification, recipient, endpoint, key_data, TTL)

    def set_form_notification(
        self,
        notification: Notification,
        endpoint: str,
        form: str,
        field: str,
    ):
        recipient = NotificationRecipient(NotificationRecipientLevel.SESSION, g.session.ID)
        key_data = {
            'form': form,
            'field': field,
        }
        TTL = g.session.expired_datetime - datetime.now()

        self.set_notification(notification, recipient, endpoint, key_data, TTL)

    def get_notifications(
        self,
        recipient: NotificationRecipient,
        endpoint: Optional[str] = None,
        key_data: Optional[dict[str, str]] = None,
    ) -> list[Notification]:
        return self._repository.get_notifications(recipient, endpoint, key_data)

    def get_form_notifications(self, endpoint: str, form: str) -> list[Notification]:
        recipient = NotificationRecipient(NotificationRecipientLevel.SESSION, g.session.ID)
        key_data = {
            'form': form,
            'field': '*',
        }

        return self.get_notifications(recipient, endpoint, key_data)
