from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from modules.User.entities.UserNameEntity import UserNameEntity


@dataclass
class UserEntity():

    ID: int
    email: Optional[str]
    name: Optional[UserNameEntity]
    is_blocked: bool
    registered_datetime: datetime
