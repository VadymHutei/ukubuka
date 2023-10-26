from datetime import datetime

from modules.Base.repositories.RedisRepository import RedisRepository
from modules.Notification.entities.Notification import Notification
from modules.Notification.entities.NotificationRecipient import NotificationRecipient


class NotificationRedisRepository(RedisRepository):

    def __init__(self):
        self._db = self._get_DB('notification')

    def _get_notification_key(
        self,
        recipient: NotificationRecipient | None,
        endpoint: str | None
    ) -> str:
        data = []

        if recipient is None:
            data.append('all')
        else:
            data.append(f'{recipient.level}_{recipient.value}')

        data.append(endpoint or 'all')

        return ':'.join(data)

    def _pop_list(self, key: str) -> list[Notification]:
        pipeline = self._db.pipeline()
        pipeline.lrange(key, 0, -1)
        pipeline.delete(key)
        data = pipeline.execute()[0]

        return [Notification.from_JSON(row.decode('utf-8')) for row in data]

    def push(self, notification: Notification):
        key = self._get_notification_key(notification.recipient, notification.endpoint)

        self._db.rpush(key, notification.to_JSON())

        if notification.expired_at is not None:
            self._db.expire(key, notification.expired_at - datetime.now())

    def pop_list(
        self,
        recipient: NotificationRecipient,
        endpoint: str | None = None,
        by_pattern: bool = False,
    ) -> list[Notification]:
        key = self._get_notification_key(recipient, endpoint)

        if by_pattern:
            notifications = []
            for key in self._db.scan_iter(key):
                notifications += self._pop_list(key)

            return notifications
        else:
            return self._pop_list(key)
