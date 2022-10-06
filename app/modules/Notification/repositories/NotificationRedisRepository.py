import json
from datetime import timedelta
from typing import Optional

from flask import g
from modules.Base.repositories.RedisRepository import RedisRepository
from modules.Notification.entities.NotificationEntity import NotificationEntity
from modules.Notification.entities.NotificationRecipient import NotificationRecipient


class NotificationRedisRepository(RedisRepository):

    def __init__(self):
        self._db = self._get_DB('notification')

    def _get_notification_key(
        self,
        endpoint: Optional[str] = None,
        form: Optional[str] = None,
        recipient: NotificationRecipient = NotificationRecipient.USER,
    ) -> str:
        data = (
            g.session.ID if recipient == NotificationRecipient.USER else 'all',
            endpoint or 'all',
            form or 'page',
        )
        return ':'.join(data)

    def add_notification(
        self,
        notification: NotificationEntity,
        endpoint: Optional[str] = None,
        form: Optional[str] = None,
        recipient: NotificationRecipient = NotificationRecipient.USER,
        TTL: Optional[timedelta] = None,
    ):
        key = self._get_notification_key(endpoint, form, recipient)

        self._db.lpush(key, json.dumps(notification.__dict__))

        if TTL:
            self._db.expire(key, TTL.total_seconds())

    def get_notifications(
        self,
        endpoint: Optional[str] = None,
        form: Optional[str] = None
    ) -> list[NotificationEntity]:
        key = self._get_notification_key(endpoint, form)
        data = self._db.lrange(key, 0, -1)

        return [NotificationEntity(**json.loads(row.decode('utf-8'))) for row in data]
