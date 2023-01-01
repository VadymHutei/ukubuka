import json
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from modules.Base.entities.AbstractJSONSerializable import AbstractJSONSerializable
from modules.Base.repositories.RedisRepository import RedisRepository
from modules.Notification.entities.NotificationRecipient import NotificationRecipient
from modules.Notification.entities.NotificationType import NotificationType


@dataclass
class Notification(AbstractJSONSerializable):

    text: str
    type: NotificationType
    recipient: Optional[NotificationRecipient] = None
    endpoint: Optional[str] = None
    expired_at: Optional[datetime] = None
    metadata: dict = field(default_factory=dict)

    def to_JSON(self) -> str:
        data = self.__dict__.copy()
        if self.recipient is not None:
            data['recipient'] = self.recipient.to_JSON()
        if self.expired_at is not None:
            data['expired_at'] = self.expired_at.strftime(
                RedisRepository.DATETIME_FORMAT)

        return json.dumps(data)

    @classmethod
    def from_JSON(cls, JSON_data: str):
        data = json.loads(JSON_data)
        if data['recipient'] is not None:
            data['recipient'] = NotificationRecipient.from_JSON(
                data['recipient'])
        if data['expired_at'] is not None:
            data['expired_at'] = datetime.strptime(
                data['expired_at'], RedisRepository.DATETIME_FORMAT)

        return cls(**data)
