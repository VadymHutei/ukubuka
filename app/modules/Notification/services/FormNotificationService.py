from flask import g
from modules.Notification.entities.Notification import Notification
from modules.Notification.entities.NotificationRecipient import NotificationRecipient
from modules.Notification.entities.NotificationRecipientLevel import NotificationRecipientLevel
from modules.Notification.services.NotificationService import NotificationService


class FormNotificationService:

    def __init__(self):
        self._notification_service = NotificationService()
        self._recipient = NotificationRecipient(NotificationRecipientLevel.SESSION, g.session.ID)

    def push(self, notification: Notification):
        notification.recipient = self._recipient
        notification.expired_at = g.session.expired_datetime

        self._notification_service.push(notification)

    def pop_list(self, endpoint: str) -> list[Notification]:
        notifications = self._notification_service.pop_list(self._recipient, endpoint)
        result = {}
        for notification in notifications:
            field = notification.metadata.get('field')
            if field is None:
                continue
            if field not in result:
                result[field] = []
            result[field].append(notification)

        return result