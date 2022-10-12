import json
from datetime import timedelta
from typing import Optional

from flask import g
from modules.Base.repositories.RedisRepository import RedisRepository
from modules.Notification.entities.NotificationEntity import Notification
from modules.Notification.entities.NotificationRecipient import NotificationRecipient


class NotificationRedisRepository(RedisRepository):

    def __init__(self):
        self._db = self._get_DB('notification')

    def _get_notification_key(
        self,
        recipient: NotificationRecipient,
        endpoint: Optional[str] = None,
        key_data: Optional[list[str]] = None,
    ) -> str:
        data = [
            f'{recipient.level}_{recipient.value}',
            endpoint or 'all',
        ]
        if key_data is not None:
            data += key_data
        return ':'.join(data)

    def _pop_notifications(self, key: str) -> list[Notification]:
        pipeline = self._db.pipeline()
        pipeline.lrange(key, 0, -1)
        pipeline.delete(key)
        data = pipeline.execute()[0]

        return [Notification(**json.loads(row.decode('utf-8'))) for row in data]

    def push_notification(
        self,
        notification: Notification,
        recipient: NotificationRecipient,
        endpoint: Optional[str] = None,
        key_data: Optional[list[str]] = None,
        TTL: Optional[timedelta] = None,
    ):
        key = self._get_notification_key(recipient, endpoint, key_data)

        self._db.rpush(key, json.dumps(notification.__dict__))

        if TTL:
            self._db.expire(key, TTL)

    def pop_notifications(
        self,
        recipient: NotificationRecipient,
        endpoint: Optional[str] = None,
        key_data: Optional[list[str]] = None,
        by_pattern: bool = False,
    ) -> list[Notification]:
        key = self._get_notification_key(recipient, endpoint, key_data)

        if by_pattern:
            notifications = []
            for key in self._db.scan_iter(key):
                notifications += self._pop_notifications(key)

            return notifications
        else:
            return self._pop_notifications(key)
