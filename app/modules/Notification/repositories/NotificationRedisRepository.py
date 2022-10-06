import json
from datetime import timedelta
from typing import Optional

from modules.Base.repositories.RedisRepository import RedisRepository
from modules.Notification.entities.NotificationEntity import NotificationEntity


class NotificationRedisRepository(RedisRepository):

    def __init__(self):
        self._db = self._get_DB('notification')

    def add_notification(
        self,
        notification: NotificationEntity,
        endpoint: Optional[str] = None,
        form: Optional[str] = None,
        TTL: Optional[timedelta] = None,
    ):
        key = ':'.join((endpoint or 'all', form or 'page'))
        self._db.lpush(key, json.dumps(notification.__dict__))
        if TTL:
            self._db.expire(key, TTL.total_seconds())
