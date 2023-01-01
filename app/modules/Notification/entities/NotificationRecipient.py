from dataclasses import dataclass
import json
from modules.Base.entities.AbstractJSONSerializable import AbstractJSONSerializable

from modules.Notification.entities.NotificationRecipientLevel import NotificationRecipientLevel


@dataclass
class NotificationRecipient(AbstractJSONSerializable):

    level: NotificationRecipientLevel
    value: str

    def to_JSON(self) -> str:
        return json.dumps({
            'level': self.level,
            'value': self.value,
        })