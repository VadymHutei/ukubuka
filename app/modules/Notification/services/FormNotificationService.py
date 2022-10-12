from datetime import datetime

from flask import g
from modules.Notification.entities.NotificationEntity import Notification
from modules.Notification.entities.NotificationRecipient import NotificationRecipient
from modules.Notification.entities.NotificationRecipientLevel import NotificationRecipientLevel
from modules.Notification.services.NotificationService import NotificationService


class FormNotificationService(NotificationService):

    def push_form_notification(self, notification: Notification, endpoint: str, form: str, field: str):
        recipient = NotificationRecipient(NotificationRecipientLevel.SESSION, g.session.ID)
        key_data = [form, field]

        TTL = g.session.expired_datetime - datetime.now()

        self.push_notification(notification, recipient, endpoint, key_data, TTL)

    def pop_form_notifications(self, endpoint: str, form: str) -> list[Notification]:
        recipient = NotificationRecipient(NotificationRecipientLevel.SESSION, g.session.ID)
        key_data = [form, '*']

        return self.pop_notifications(recipient, endpoint, key_data, by_pattern=True)
