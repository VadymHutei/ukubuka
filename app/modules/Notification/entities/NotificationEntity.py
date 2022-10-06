from dataclasses import dataclass
from typing import Any, Optional

from modules.Notification.entities.NotificationType import NotificationType


@dataclass
class NotificationEntity:

    text: str
    type: str = NotificationType.INFO_TYPE
    metadata: Optional[dict[str, Any]] = None
