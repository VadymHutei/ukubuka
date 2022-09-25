from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class SessionEntity:

    ID: str
    created_datetime: datetime
    expired_datetime: datetime
    user_agent: Optional[str]
    is_new: bool = False
