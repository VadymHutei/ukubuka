from modules.Notification.entities.Notification import Notification
from modules.Notification.entities.NotificationRecipient import NotificationRecipient
from modules.Notification.repositories.NotificationRedisRepository import NotificationRedisRepository


class NotificationService:

    def __init__(self):
        self._repository = NotificationRedisRepository()

    def push(self, notification: Notification):
        self._repository.push(notification)

    def pop_list(
        self,
        recipient: NotificationRecipient,
        endpoint: str|None = None,
        by_pattern: bool = False,
    ) -> list[Notification]:
        return self._repository.pop_list(recipient, endpoint, by_pattern)
